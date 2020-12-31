from os import getcwd

from modulos.txt import ArchivoTxt


class Configuracion:

    def __init__(self):
        pass

    def cargar_opciones(self):
        opciones = dict()

        ruta_Actual  = ( getcwd ())
        txt = ArchivoTxt(ruta_Actual + '\\' + 'config.txt')
        contenido = txt.leer()

        for conte in contenido:
            print(conte)

            clave, parametro = conte.split(':')
            opciones [clave] = str(parametro)

        return opciones





    def guardar_opciones(self):
        pass