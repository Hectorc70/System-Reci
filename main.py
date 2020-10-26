from os.path import exists

import eel

from respaldar.reci_xml import TimbreCop
from respaldar.reci_xml import Recibo

from modulos.rutas import abrir_directorio, abrir_archivo
from modulos.txt import ArchivoTxt

from datos.recibo import ReciboNomina, RutaRecibo
from datos.metadatos import ReciMetadatos
from modulos.periodos import armar_periodos_intermedios, armar_periodos

from herramientas.directorio import Directorio
eel.init('web_folder', allowed_extensions=['.js','.html'])
"""
**---------------------------------------------------------------------------------------------**
                        ***PRUEBAS***
**---------------------------------------------------------------------------------------------**
"""
def ejecutar(ruta, periodo, anno, ruta_destino):
    timbre = TimbreCop(ruta, periodo, anno, ruta_destino)
    timbre.copiado_archivos()

ruta = 'Y:/CFDI_2020/CFDI_NOMINA_2020'
ruta_destino = 'X:/CFDI_NOMINA_2020'
ejecutar(ruta, '01',  '2020', ruta_destino)

"""
**---------------------------------------------------------------------------------------------**
                        ***HERRAMIENTAS***
**---------------------------------------------------------------------------------------------**
"""
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
def rutas_recibos_orig(ruta, anno, periodo):  

    originales = ArchivosOrig(ruta, anno, periodo)
    recibos = originales.archivos_pdf()

    return recibos

@eel.expose
def copiado_recibos(carpt_orig, carpt_dest ,archivos):
    
    for archivo in archivos:
        datos = archivo.split('\\')
        nombre = datos[-1]

        reci = ArchivoRecibo(carpt_orig, archivo,carpt_dest, nombre, True)
        reci.comprobar_acciones()
    
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
    rutas = ruta_archivos.recuperacion()
    
    return rutas
    

@eel.expose
def guardar_mdatos(rutas, anno):
    for ruta in rutas:
        recibo = ReciboNomina(ruta)
        metadatos_recibos = recibo.almacenar_datos()

        mtdatos = ReciMetadatos(metadatos_recibos, anno)
        mtdatos.guardar()
        print("Datos Procesados: " + ruta)
    
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
        datos = ReciMetadatos('', a_ini)
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
    
    datos = ReciMetadatos('', '')
    datos.consultar_extraer_recibos(ids, ruta_guardado)

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