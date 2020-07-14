import eel

from metadatos.ayuda.rutas import Rutas, abrir_directorio

eel.init('web_folder', allowed_extensions=['.js','.html'])



@eel.expose
def ruta_metadatos(): 
    directorio = abrir_directorio()
    r_metadatos = Rutas(directorio)
    rutas = r_metadatos.recuperar_rutas()
    
    print(directorio)
    return directorio
    


try:
    eel.start('main.html')


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")