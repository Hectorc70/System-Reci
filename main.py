import eel
from os.path import exists
from metadatos.ayuda.rutas import Rutas, abrir_directorio
from metadatos.recibo import ReciboNomina, rutas_recibos
from metadatos.metadatos import ReciMetadatos
eel.init('web_folder', allowed_extensions=['.js','.html'])



@eel.expose
def ruta_metadatos(): 
    directorio = abrir_directorio()    
    
    if exists(directorio):
        return directorio
    else:
        return ''

@eel.expose
def mostrar_rutas_recibos(directorio, anno, periodo):
    rutas = rutas_recibos(directorio, anno, periodo)
    
    return rutas
    

@eel.expose
def guardar_mdatos(rutas, anno):
    for ruta in rutas:
        recibo = ReciboNomina(ruta)
        metadatos_recibos = recibo.formateo_datos()

        mtdatos = ReciMetadatos(metadatos_recibos, anno)
        errores = mtdatos.guardar()

        if errores:
            return errores
        else:
            True
try:
    eel.start('main.html')


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")