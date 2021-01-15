from os.path import exists

import eel
import os.path

from modulos.rutas import abrir_directorio, abrir_archivo, unir_cadenas
from modulos.txt import ArchivoTxt
from modulos.periodos import armar_periodos_intermedios, armar_periodos
from modulos.archivo import Archivo
from modulos.log import Log

from almacenar.cliente import Cliente
from configuraciones import Configuracion
from almacenar.registro import RegistroRecibo, RegistroEmpleado
from almacenar.ayuda.recibo import RutaRecibo
from almacenar.empleado import DatosEmpleados


from respaldar.reci_xml import TimbreCop, ReciboCop
from respaldar.originales import ArchivoTimbre, ArchivoRecibo


from herramientas.directorio import Directorio
eel.init('web_folder', allowed_extensions=['.js', '.html'])
"""
**---------------------------------------------------------------------------------------------**
                        ***PRUEBAS***
**---------------------------------------------------------------------------------------------**
"""
""" def ejecutar(ruta, periodo, anno, ruta_destino):
    timbre = TimbreCop(ruta, periodo, anno, ruta_destino)
    timbre.copiado_archivos()

ruta = 'Y:/CFDI_2020/CFDI_NOMINA_2020'
ruta_destino = 'X:/CFDI_NOMINA_2020'
ejecutar(ruta, '01',  '2020', ruta_destino) """

"""
**---------------------------------------------------------------------------------------------**
                        ***HERRAMIENTAS***
**---------------------------------------------------------------------------------------------**
"""


def leer_config_bd():
    opciones = Configuracion()
    opciones_param = opciones.cargar_opciones()

    if opciones_param:       

        return opciones_param

    else: 
        print("No existen configuraciones")



@eel.expose
def directorios(ruta1, ruta2):
    directorio_orig = Directorio(ruta1)
    directorio_dos = Directorio(ruta2)

    dif_rutas1 = directorio_orig.comparar_directorios(
        directorio_dos.rutas_sin_base)
    # dif_rutas2 = directorio_dos.comparar_directorios(directorio_orig.contenido)

    return dif_rutas1


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
def rutas_timbres_orig(ruta, periodo, anno):

    originales = ArchivoTimbre(ruta, periodo, anno)
    timbres = originales.recuperar_timbres()            

    return timbres


@eel.expose
def copiar_timbres(carpeta_origen, carpt_dest, archivos, anno, periodo):

    for archivo in archivos:

        timbre = TimbreCop(carpeta_origen, periodo, anno, carpt_dest)
        timbre.copiado_archivos(archivo)

    return True


@eel.expose
def rutas_recibos_orig(ruta, anno, periodo):

    originales = ArchivoRecibo(ruta, anno, periodo)
    recibos = originales.recuperar_recibos()

    return recibos


@eel.expose
def copiado_recibos(carpt_orig, carpt_dest, archivos):

    for archivo in archivos:

        reci = ReciboCop(carpt_orig, archivo, carpt_dest)
        reci.separar_en_recibos()

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
                        ***ALMACENAR DATOS EN BASE DE DATOS***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def mostrar_rutas_recibos(directorio, anno, periodo):
    ruta_archivos = RutaRecibo(directorio, anno, periodo)
    rutas = ruta_archivos.recuperar_periodo()

    return rutas


@eel.expose
def guardar_mdatos(archivos_pdf):
    opciones = Configuracion()
    opciones_param = opciones.cargar_opciones()

    if opciones_param:
        ip = opciones_param['SERVER-HOST']
        puerto = opciones_param['PUERTO']
        usuario = opciones_param['USUARIO']
        psw = opciones_param['PSWORD']
        bd = opciones_param['BASE-DATOS']

    for datos in archivos_pdf:
        archivo = datos[-1].split('/')[-1]
        control = archivo.split('_')[0]
        periodo = str(datos[1]) + str(datos[0])

        recibo = RegistroRecibo(control, periodo,datos[2], archivo, datos[-1])
        cadena_accion = recibo.guardar()
        conexion = Cliente(ip, int(puerto), usuario, psw, bd, 'recibos')
        respuesta = conexion.enviar_datos(cadena_accion)
        conexion.cerrar_conexion()

        print(respuesta)
        print("Datos Procesados: {}".format(datos))

    

    return True

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
try:
    opciones = [{'size':(1080, 720)}]

    eel.start('main.html')


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")
