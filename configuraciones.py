from modulos.txt import ArchivoTxt


class Configuracion:

    def __init__(self):
        pass

    def cargar_opciones(self):
        opciones = dict()


        txt = ArchivoTxt('config.txt')
        contenido = txt.leer()

        for conte in contenido:
            print(conte)

            clave, parametro = conte.split(':')
            opciones [clave] = str(parametro)

        return opciones





    def guardar_opciones(self):
        pass