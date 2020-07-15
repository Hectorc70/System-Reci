import eel

from metadatos.ayuda.rutas import Rutas, abrir_directorio
from metadatos.recibo import ReciboNomina, rutas_recibos
eel.init('web_folder', allowed_extensions=['.js','.html'])



@eel.expose
def ruta_metadatos(): 
    directorio = abrir_directorio()    
    rutas_recibos(directorio)
    print(directorio)
    return directorio
"""
def ejecutar()   
reci = ReciboNomina()
    rutas = rutas_recibos(directorio)   
    
"""

try:
    eel.start('main.html')


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")