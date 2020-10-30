from shutil import copy
from os.path import exists
from os import makedirs

from modulos.rutas import unir_cadenas, crear_directorio



class Archivo:
    """Clase que trata con archivos, copia, mueve.

    origen: ruta_origen, destino=ruta_destino, las rutas deben ser la ruta
    completa(C:/ORIGEN/ARCHIVO.pdf, C:/DESTINO/ARCHIVO_copia.pdf).

    Crea automaticamente la carpeta de destino de 
    la copia.
    """


    def __init__(self, origen, destino, copiar=False, mover=False):
        self.ruta_archivo_origen = origen        
        self.ruta_archivo_destino = destino        
        self.copiar = copiar
        self.mover = mover

        
    def comprobar_acciones(self):
            if self.copiar:
                self.copiar_archivo()
            elif self.mover == True and self.copiar == False:
                self.mover_archivo()

    def cambiar_nombre(self):
        pass

    def copiar_archivo(self):
        carpeta = self.ruta_archivo_destino.split('/')[:-1]
        carpeta = unir_cadenas('/', carpeta)
        crear_directorio(carpeta) 

        copy(self.ruta_archivo_origen, self.ruta_archivo_destino)


    def mover_archivo(self):
        pass
    
    