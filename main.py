import eel

from metadatos.ayuda.rutas import Rutas, abrir_directorio
from metadatos.recibo import ReciboNomina, rutas_recibos
eel.init('web_folder', allowed_extensions=['.js','.html'])



@eel.expose
def ruta_metadatos(): 
    directorio = abrir_directorio()    
    
    return directorio

@eel.expose
def mostrar_rutas_recibos(directorio):
    rutas = rutas_recibos(directorio)
    
    return rutas
    

@eel.expose
def recopilacion_metadatos(rutas):
    for ruta in rutas:
        recibo = ReciboNomina(ruta)
        texto = recibo.buscar_datos()
        print(texto)

try:
    eel.start('main.html')


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")