from os.path import exists

import eel

from respaldar.reci_xml import ArchivosOrig
from modulos.rutas import abrir_directorio
from datos.recibo import ReciboNomina, RutaRecibo
from datos.metadatos import ReciMetadatos
from modulos.periodos import armar_periodos_intermedios, armar_periodos

eel.init('web_folder', allowed_extensions=['.js','.html'])
"""
**---------------------------------------------------------------------------------------------**
                        ***RESPALDAR XML Y RECIBOS***
**---------------------------------------------------------------------------------------------**
"""

@eel.expose
def rutas_recibos_orig():
    ruta = 'Y:\CFDI_2020\CFDI_NOMINA_2020'
    anno = '2020'
    perio = '01'

    originales = ArchivosOrig(ruta, anno, perio)
    recibos = originales.archivos_pdf()

    return recibos


"""
**---------------------------------------------------------------------------------------------**
                        ***RECOPILADOR***
**---------------------------------------------------------------------------------------------**
"""
@eel.expose
def ruta_metadatos(): 
    directorio = abrir_directorio()    
    
    if exists(directorio):
        return directorio
    else:
        return ''

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
    
    print('------------------ SE PROCESARON TODOS LOS ARCHIVOS SELECCIONADOS -------------------------')

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

        return recibos

@eel.expose
def buscador_recibo(ids, ruta_guardado):
    """llama al metodo que busca registros
    en la base de datos pasando como parametro el id
    del registro de la bd"""  
    
    datos = ReciMetadatos('', '')
    datos.consultar_extraer_recibos(ids, ruta_guardado)

    print('Archivos Guardados en: ' + ruta_guardado)
    
    return True



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