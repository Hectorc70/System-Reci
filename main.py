from os.path import exists
from os import startfile
from os import getpid
import tempfile 

import eel
import os.path

from login.login import User, ArchivoTemp, Token

from modulos.rutas import abrir_directorio, abrir_archivo, unir_cadenas
from modulos.txt import ArchivoTxt
from modulos.periodos import armar_periodos_intermedios, armar_periodos
from modulos.archivo import Archivo
from modulos.log import Log

from respaldar.reci_xml import TimbreCop, ReciboCop
from respaldar.originales import ArchivoTimbre, ArchivoRecibo, ArchivosOrig

from validacion.validacion import ArchivosPorValidar, ArchivosValidados

from subir.cliente import Cliente
from subir.empleado import DatosEmpleados
from subir.recibo import RutaRecibo

from buscador.cliente import ClienteBuscador


from herramientas.directorio import Directorio
eel.init('web_folder', allowed_extensions=['.js', '.html'])

file_data_user = ArchivoTemp()
@eel.expose    
def leer_config_bd():
    opciones = Configuracion()
    opciones_param = opciones.cargar_opciones()

    if opciones_param:       

        return opciones_param

    else: 
        print("No existen configuraciones")




"""
**---------------------------------------------------------------------------------------------**
                        ***GENERALES***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def enviar_ruta():
    directorio = abrir_directorio()

    if exists(directorio):
        return directorio
    else:
        return ''


@eel.expose
def enviar_ruta_archivo():
    ruta = abrir_archivo()

    return ruta


"""
**---------------------------------------------------------------------------------------------**
                        ***RESPALDAR XML Y RECIBOS***
**---------------------------------------------------------------------------------------------**
"""
@eel.expose
def enviar_rutas(ruta, periodo, anno):
    rutas_timbres = rutas_timbres_orig(ruta, periodo, anno)
    rutas_recibos = rutas_recibos_orig(ruta, periodo, anno)

    return [rutas_timbres, rutas_recibos]
@eel.expose
def rutas_timbres_orig(ruta, periodo, anno):

    originales = ArchivoTimbre(ruta, periodo, anno)
    timbres = originales.recuperar_timbres()            

    return timbres
    

@eel.expose
def rutas_recibos_orig(ruta, periodo,anno):

    originales = ArchivoRecibo(ruta, anno, periodo)
    recibos = originales.recuperar_recibos()

    return recibos

@eel.expose
def respaldar(tipo, carpeta_origen, ruta_archivo, carpt_dest , periodo, anno):
    

    
    
    if tipo == 'timbres':
        respaldar_timbres(carpeta_origen, carpt_dest,ruta_archivo)

    elif tipo == 'recibos':
        respuesta = respaldar_recibos(carpeta_origen,ruta_archivo, carpt_dest,periodo, anno)

        return respuesta
@eel.expose
def respaldar_timbres(carpeta_origen, carpt_dest, archivo,):
        timbre = TimbreCop(carpeta_origen, carpt_dest)
        timbre.copiado_archivos(archivo)




@eel.expose
def respaldar_recibos(carpeta_original, ruta_archivo, carpt_destino, periodo, anno):
    periodo_copiado = ArchivoTimbre(carpt_destino, periodo, anno)
    timbres_nombres = periodo_copiado.recuperar_timbres_nombres()
    
    if timbres_nombres:
        reci = ReciboCop(carpeta_original, ruta_archivo, carpt_destino)
        reci.separar_en_recibos(timbres_nombres)
        return ['EXITOSO', True]
    else:
        return ['ERROR', True]
        
@eel.expose
def leer_log_recibos():
    try:
        log = Log('Log-copiado-Recibos.txt')   
        errores = log.devolver_datos('ERROR')
        if errores:
            
            return ['ERRORES', True]
            
        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]
    
    except:
        return[' ', False]


"""
**---------------------------------------------------------------------------------------------**
                        ***VALIDAR XML Y RECIBOS***
**---------------------------------------------------------------------------------------------**
"""

@eel.expose
def mostrar_archivos(ruta, anno, periodo):
    archivos_orig = ArchivosOrig(ruta, periodo, anno)

    rutas = archivos_orig.depurar_rutas()

    recibo  = ArchivosPorValidar(ruta, rutas[0])
    recibos = recibo.depurar_archivos()

    timbre  = ArchivosPorValidar(ruta, rutas[1])
    timbres = timbre.depurar_archivos()



    return [recibos, timbres]

@eel.expose
def validar_archivos(timbres, recibos):

    archivos = ArchivosValidados(timbres, recibos)

    archivos_validados = archivos.validar()

    
    return archivos_validados


"""
**---------------------------------------------------------------------------------------------**
                        ***ALMACENAR DATOS EN BASE DE DATOS***
**---------------------------------------------------------------------------------------------**
"""

#RECIBOS DE NOMINA
@eel.expose
def mostrar_rutas_recibos(directorio, anno, periodo):
    ruta_archivos = RutaRecibo(directorio, anno, periodo)
    rutas = ruta_archivos.recuperar_periodo()

    return rutas


@eel.expose
def guardar_mdatos_recibos(datos_archivos_pdf):
    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        
        for datos in datos_archivos_pdf:
            control = int(datos[0].split('_')[0])
            datos_format = {
                'archivo':datos[0],
                'ruta':datos[-1],
                'periodo':datos[1],
                'nomina':datos[2],
                'control':str(control)
            }
            

            cliente = Cliente(token[1])
            cliente.enviar_datos_recibo(datos_format)

        return True     
    else:
        return 'ERROR'


@eel.expose
def leer_log_recibos_subidos():
    try:
        log = Log('Log_Set_Recibos_Data.txt')   
        errores = log.devolver_datos('ERROR')
        if errores:
            log.abrir_log()
            return ['ERRORES', True]

        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]
    
    except:
        return[' ', False]

#EMPLEADOS
@eel.expose
def mostrar_datos_empleados(ruta):   

    empleados = DatosEmpleados(ruta)
    datos = empleados.leer_datos_empleados()

    return datos

@eel.expose
def subir_datos_empleados(datos_empleados):   
    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()

        for datos in datos_empleados:
            datos_format = {
                'control':datos[0],
                'nombre':datos[1],
                'ape_p':datos[2],
                'ape_m':datos[3],
            }
            

            cliente = Cliente(token[1])
            cliente.enviar_datos_empleado(datos_format)

        return ''
    else:
        return 'ERROR'

@eel.expose
def leer_log_empleados_subidos():
    try:
        log = Log('Log_Set_Empleados_Data.txt')   
        errores = log.devolver_datos('ERROR')
        if errores:
            log.abrir_log()
            return ['ERRORES', True]

        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]
    
    except:
        return[' ', False]

"""
**---------------------------------------------------------------------------------------------**
                        ***BUSCADOR***
**---------------------------------------------------------------------------------------------**
"""



    

def comprobar_fechas(**kwargs):
        """Busca recibos de los periodos
        indicados pasados como parametros"""

        if kwargs['anno_inicial'] == kwargs['anno_final']:

            periodos = armar_periodos(kwargs['anno_inicial'],
                                    kwargs['periodo_inicial'],
                                    kwargs['periodo_final'], True)          

            return [periodos]

        elif int(kwargs['anno_inicial']) + 1 == int(kwargs['anno_final']):

            periodos_ini = armar_periodos(kwargs['anno_inicial'],
                                        kwargs['periodo_inicial'],format=True)

            periodos_finales = armar_periodos(kwargs['anno_final'],
                                            ultimo_periodo=kwargs['periodo_final'], format=True)   

            return [periodos_ini, periodos_finales]

        else:
            periodos_ini = armar_periodos(kwargs['anno_inicial'],
                                        kwargs['periodo_inicial'], format=True)

            periodos_interm = armar_periodos_intermedios(kwargs['anno_inicial'],
                                                        kwargs['anno_final'], True)

            periodos_finales = armar_periodos(kwargs['anno_final'],
                                            ultimo_periodo=kwargs['periodo_final'], format=True)

            return [periodos_ini, periodos_interm, periodos_finales]




@eel.expose
def recuperar_por_nombre(nombre, ape_p, ape_m, periodo_i, anno_i, periodo_f, anno_f):
    data = file_data_user.get_data_user()
    periodos = comprobar_fechas(anno_inicial=anno_i, periodo_inicial=periodo_i,
                        periodo_final=periodo_f, anno_final=anno_f)

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()

        
        cliente  = ClienteBuscador(token)
        control = cliente.recuperar_control()
    
    if control:
        for periodo in periodos:


            pass



@eel.expose
def recuperar_por_control(control, periodo_i, anno_i, periodo_f, anno_f):
    def formatear_datos(periodos_datos_recibos):
        
        for datos_recibos in periodos_datos_recibos:

            for keys in datos_recibos.keys():
                id_recibo = datos_recibos['id_recibo']
                control = datos_recibos['no_control']
                periodo = datos_recibos['periodo']
                nomina = datos_recibos['tipo_nomina']

                return [id_recibo, control, periodo, nomina]
            
    
    
    
    
    
    data = file_data_user.get_data_user()
    annos = comprobar_fechas(anno_inicial=anno_i, periodo_inicial=periodo_i,
                        periodo_final=periodo_f, anno_final=anno_f)


    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        cliente = ClienteBuscador(token[1])


        datos_recuperados = list()
        for anno in annos:
            for periodos in anno.values():
                for periodo in periodos:
                    resp = cliente.recuperar_datos_recibo(control, periodo)
                    if resp[0] ==200:
                        datos_format = formatear_datos(resp[1])
                        datos_recuperados.append(datos_format)

        return datos_recuperados

    else:
        return 'ERROR'





@eel.expose
def recuperar_recibo(id_recibo):
    """llama al metodo que retorna el recibo
    de nomina con el id pasado como parametro
    """

    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        cliente = ClienteBuscador(token[1])

        resp = cliente.recuperar_recibo(id_recibo)

        if resp[0] == 200:
            return resp



"""
**---------------------------------------------------------------------------------------------**
                        ***CONFIG EEL***
**---------------------------------------------------------------------------------------------**
"""
@eel.expose
def login_user(control, password):

        user = User()
        resp = user.get_database_user(control, password)
        if resp[0] == 200:
            file_data_user.save_data_user(control, password)
        
        return resp


try:
    opciones = [{'size':(1080, 720)}]

    eel.start('login.html', port=8080)
    

except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")

