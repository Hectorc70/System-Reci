from modulos.rutas import Rutas


class Directorio(Rutas):
    def __init__(self, directorio):
        Rutas.__init__(self)
        self.directorio = directorio
        self.rutas = self.directorios()
        self.rutas_sin_base = self.quitar_ruta_base()

    def directorios(self):
        carpetas = self.recuperar_rutas(self.directorio, split=False)

        return carpetas

    
    def quitar_ruta_base(self):
        """Le Quita a cada ruta su ruta base
            ejemplo: ruta = 'C:\\prueba\\archivo.txt', ruta_base=C:\\prueba
            Retorna: ruta_sin_base = '\\archivo.txt'"""

        
        rutas_sin_base = list()

        for ruta in self.rutas:
            ruta = ruta.replace(self.directorio.replace('/','\\'), '')
            rutas_sin_base.append(ruta)
        
        return rutas_sin_base

    def comparar_directorios(self, directorios2):
        """Retorna las rutas que no estan en la lista pasada 
            como parametro.
            Parametros: directorio2 =  tipo 'list, deben ser rutas
            sin su ruta base"""
        
        rutas_dif = list()

        for ruta in self.rutas_sin_base:
            if ruta not in directorios2:
                rutas_dif.append(ruta)

        return rutas_dif
