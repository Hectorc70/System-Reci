from shutil import copy
from os.path import exists
from os import makedirs

from modulos.rutas import unir_cadenas, crear_directorio
class Archivo:
    def __init__(self, origen, destino, nombre, cop=False, mov=False):
        self.origen = origen        
        self.destino = destino     
        self.nombre = nombre
        self.copiar = cop
        self.mover = mov

        
    def comprobar_acciones(self):
            if self.copiar:
                self.copiar_archivo()
            elif self.mover == True and self.copiar == False:
                self.mover_archivo()

    def cambiar_nombre(self):
        pass

    def copiar_archivo(self):
        carpeta = self.destino.split('\\')[0:-1]
        carpeta = unir_cadenas('\\', carpeta)
        if exists(carpeta):
            
            copy(self.origen, self.destino)
        else:           
            crear_directorio(carpeta)       
            self.copiar_archivo()


    def mover_archivo(self):
        pass
    
    