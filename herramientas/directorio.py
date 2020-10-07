from modulos.rutas import Rutas


class Directorio(Rutas):
    def __init__(self, ruta):
        Rutas.__init__(self)
        self.ruta = ruta
        self.contenido = self.directorios()
    
    def directorios(self):        
        carpetas = self.recuperar_rutas(self.ruta, split=False)
        
        return carpetas


    def comparar_directorios(self, directorio2):
        """Compara dos directorios el parametro
        directorio2:  tipo 'list'"""
        
        rutas_dif = list()
        
        for ruta in self.contenido:

            if self.contenido not in directorio2:
                rutas_dif.append(ruta)

        return rutas_dif