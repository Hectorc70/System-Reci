from os.path import exists

import eel

from modulos.cliente import Cliente
from configuraciones import Configuracion

from respaldar.reci_xml import TimbreCop, ReciboCop
from respaldar.originales import ArchivoTimbre, ArchivoRecibo 

from modulos.rutas import abrir_directorio, abrir_archivo
from modulos.txt import ArchivoTxt

from datos.ayuda.recibo import RutaRecibo, NuevoReciNom
from datos.metadatos import ReciMetadatos
from modulos.periodos import armar_periodos_intermedios, armar_periodos

from herramientas.directorio import Directorio
eel.init('web_folder', allowed_extensions=['.js','.html'])
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

def comprobar_conexiones():
    opciones = Configuracion()
    opciones_param = opciones.cargar_opciones()
    
    if opciones_param:
        ip = opciones_param['SERVER-HOST']        
        puerto = opciones_param['PUERTO']
        usuario = opciones_param['USUARIO']
        psw = opciones_param['PSWORD']
        bd = opciones_param['BASE-DATOS']
        tabla = opciones_param['TABLA']
        accion = "CONSULTAR:control = 318212 AND anno ='2020'|control, periodo, anno, ruta"
        conexion = Cliente(ip, int(puerto), usuario, psw, bd, tabla, accion)
        cliente = conexion.conectar()
        
        if cliente == True:       
            return True
        else:
            print('Conexion con servidor no exitosa')
            

comprobar_conexiones()

@eel.expose
def directorios(ruta1, ruta2):
    directorio_orig = Directorio(ruta1)
    directorio_dos= Directorio(ruta2)

    dif_rutas1 = directorio_orig.comparar_directorios(directorio_dos.rutas_sin_base)
    #dif_rutas2 = directorio_dos.comparar_directorios(directorio_orig.contenido)

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
def rutas_timbres_orig(ruta,periodo, anno):  

    originales = ArchivoTimbre(ruta, periodo, anno)
    timbres = originales.recuperar_timbres()

    return timbres


@eel.expose
def copiar_timbres(carpeta_origen,carpt_dest, archivos, anno, periodo):

    for archivo in archivos:

        timbre = TimbreCop(carpeta_origen, periodo,anno, carpt_dest)
        timbre.copiado_archivos(archivo)

    return True


@eel.expose
def rutas_recibos_orig(ruta, anno, periodo):  

    originales = ArchivoRecibo(ruta, anno, periodo)
    recibos = originales.recuperar_recibos()

    return recibos

@eel.expose
def copiado_recibos(carpt_orig, carpt_dest ,archivos):
    
    for archivo in archivos:   

        reci = ReciboCop(carpt_orig, archivo,carpt_dest)
        reci.separar_en_recibos()
    
    print("Archivos copiados")
    return True

"""
**---------------------------------------------------------------------------------------------**
                        ***RECOPILADOR***
**---------------------------------------------------------------------------------------------**
"""

@eel.expose
def mostrar_rutas_recibos(directorio, anno, periodo):
    ruta_archivos =  RutaRecibo(directorio, anno, periodo)
    rutas = ruta_archivos.recuperar_periodo()
    
    return rutas
    

@eel.expose
def guardar_mdatos(archivos_pdf):
    for datos in archivos_pdf:    

        mtdatos = ReciMetadatos(datos)
        mtdatos.guardar()
        print("Datos Procesados: {}".format(datos[-1]))
    
    return True
    

"""
**---------------------------------------------------------------------------------------------**
                        ***BUSCADOR***
**---------------------------------------------------------------------------------------------**
"""

@eel.expose
def obtener_reci_buscados(control, p_ini, a_ini, p_fin, a_fin):
    if a_ini == a_fin:
        periodos = armar_periodos(a_ini, periodo_ini=p_ini, ultimo_periodo=p_fin)
        datos = ReciMetadatos(datos='')
        recibos = datos.devolver_datos(control, a_ini, periodos)
        
        if recibos:
            return recibos
        else:
            return False

@eel.expose
def buscador_recibo(ids, ruta_guardado):
    """llama al metodo que busca registros
    en la base de datos pasando como parametro el id
    del registro de la bd"""  
    
    datos = ReciMetadatos('')
    datos.extraer_recibos(ids, ruta_guardado)

    print('Archivos Guardados en: ' + ruta_guardado)
    
    
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
    opciones = ["--start-fullscreen"]
    
    eel.start('main.html', cmdline_args=opciones)


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")