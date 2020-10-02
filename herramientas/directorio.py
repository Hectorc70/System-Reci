from modulos.rutas import Rutas


class Directorio(Rutas):
    def __init__(self, ruta):
        Rutas.__init__(self)
        self.ruta = ruta

    def directorios(self):

        carpetas = self.recuperar_carpetas(self.ruta, carpeta_1=True)
        print(carpetas)
