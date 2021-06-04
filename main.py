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


from configuraciones import Configuracion
from almacenar.registro import RegistroRecibo, RegistroEmpleado
from almacenar.ayuda.recibo import PERIODOS, RutaRecibo
from almacenar.empleado import DatosEmpleados


from respaldar.reci_xml import TimbreCop, ReciboCop
from respaldar.originales import ArchivoTimbre, ArchivoRecibo, ArchivosOrig
from validacion.validacion import ArchivosPorValidar, ArchivosValidados

from subir.cliente import Cliente

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
            datos_format = {
                'archivo':datos[0],
                'ruta':datos[-1],
                'periodo':datos[1],
                'nomina':[2],
                'control':datos[0].split('_')[0]
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

@eel.expose
def guardar_empleados(ruta):   
    datos = DatosEmpleados(ruta)
    datos_empleados = datos.leer_datos_empleados()

    opciones_param = leer_config_bd()   
    ip = opciones_param['SERVER-HOST']
    puerto = opciones_param['PUERTO']
    usuario = opciones_param['USUARIO']
    psw = opciones_param['PSWORD']
    bd = opciones_param['BASE-DATOS']
    
    for dato in datos_empleados:
        registro = RegistroEmpleado(dato[0], dato[1], dato[2], dato[3])
        query_empleado = registro.guardar()
        conexion = Cliente(ip, int(puerto), usuario, psw, bd, 'empleados')
        respuesta = conexion.enviar_datos(query_empleado)
        conexion.cerrar_conexion()
    


    print('PROCESO TERMINADO')
    return True




"""
**---------------------------------------------------------------------------------------------**
                        ***BUSCADOR***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def mostrar_datos_encontrados(control, nombre, periodo_i, anno_i, periodo_f, anno_f):
    """ Devuelve todos los datos encontrados de acuerdo a los parametros
    pasados
    """
    
    opciones_param = leer_config_bd()

    ip = opciones_param['SERVER-HOST']
    puerto = opciones_param['PUERTO']
    usuario = opciones_param['USUARIO']
    psw = opciones_param['PSWORD']
    bd = opciones_param['BASE-DATOS']

    def comprobar_fechas(**kwargs):
        """Busca recibos de los periodos
        indicados pasados como parametros"""

        periodos_por_buscar = list()

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


    def convertir_datos(datos_encontrados):

        datos_format = list()  

        for registros in datos_encontrados:    
            if ',' in registros:
                registros_datos = registros.split(',')

                for datos_r in registros_datos:
                    datos = datos_r.split('|')

                    datos_format.append(datos)
            if ',' not in registros:
                datos = registros.split('|')
                datos_format.append(datos)

                
        return datos_format

    if control != '':
        annos_periodos = comprobar_fechas(anno_inicial=anno_i, periodo_inicial=periodo_i,
                        periodo_final=periodo_f, anno_final=anno_f)

        campos = "empleados.NoControl, recibos.Periodo, recibos.TipoNomina, recibos.IdRecibo, recibos.RutaArchivo"
        
        datos_encontrados = list()
        for anno_per in annos_periodos:
            for anno , periodos in anno_per.items():
                for periodo in periodos: 
                    conexion = Cliente(ip, int(puerto), usuario, psw, bd, 'empleados')                   
                    condiciones = "ON empleados.NoControl = recibos.NoControl WHERE empleados.NoControl = '{}' AND recibos.Periodo='{}'".format(control, periodo)
                    empleado = RegistroEmpleado(control,'','','')
                    query_consulta = empleado.consultar(campos, condiciones)                   
                    respuesta = conexion.enviar_datos(query_consulta)
                    conexion.cerrar_conexion()
                    
                    if respuesta != '':                        
                        datos_encontrados.append(respuesta)

                    else:
                        continue
        
        if datos_encontrados:
            datos = convertir_datos(datos_encontrados)
            return datos
        else:
            return False


    elif control =='':
        pass


@eel.expose
def abrir_recibo(ruta):


    import os
    os.startfile(ruta)




@eel.expose
def recuperar_recibos(datos, ruta_guardado):
    """llama al metodo que busca registros
    en la base de datos pasando como parametro el id
    del registro de la bd"""

    for dato_ruta in datos:
        archivo = dato_ruta[1].split('/')[-1]
        ruta_destino = ruta_guardado + '/' + dato_ruta[0] + '/' +archivo
        nuevo_archivo = Archivo(dato_ruta[1], ruta_destino, copiar=True)
        nuevo_archivo.comprobar_acciones()

    print('Archivos Guardados en: ' + ruta_guardado)

    """  import os
    # Abre una carpeta del escritorio en el explorador.
    
    os.system(f'start {os.path.realpath(ruta_guardado)}') """
    
    return True


@eel.expose
def leer_txt(ruta):
    txt = ArchivoTxt(ruta)
    contenido = txt.leer()

    print(contenido)
    return contenido


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
file_data_user.close_temp()
print("ventana cerrada")

