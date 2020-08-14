import eel
from os.path import exists
from metadatos.ayuda.rutas import Rutas, abrir_directorio
from metadatos.recibo import ReciboNomina, RutaRecibo
from metadatos.metadatos import ReciMetadatos
from buscar.ayuda.periodos import armar_periodos_intermedios, armar_periodos

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
    ruta_archivos =  RutaRecibo(directorio, anno, periodo)
    rutas = ruta_archivos.recuperacion()
    
    return rutas
    

@eel.expose
def guardar_mdatos(rutas, anno):
    for ruta in rutas:
        recibo = ReciboNomina(ruta)
        metadatos_recibos = recibo.formateo_datos()

        mtdatos = ReciMetadatos(metadatos_recibos, anno)
        mtdatos.guardar()
@eel.expose
def buscador_recibo(control, p_ini, a_ini, p_fin, a_fin, auto_extraer=True):
    if a_ini == a_fin:
        periodos = armar_periodos(a_ini, periodo_ini=p_ini, ultimo_periodo=p_fin)

    elif a_ini != a_fin:
        periodos_inter = armar_periodos_intermedios(a_ini, a_fin)
        periodos_ini = armar_periodos(a_ini, periodo_ini=p_ini)
        periodos_fin = armar_periodos(a_fin, ultimo_periodo=p_fin)
        
    

    
    


try:
    opciones = ["--start-fullscreen"]
    
    eel.start('main.html', cmdline_args=opciones)


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")