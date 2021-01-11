from os import getcwd

from modulos.txt import ArchivoTxt
from modulos.fechas import RangoFechas

class Log(ArchivoTxt):

    def __init_(self, nombre):
        self.ruta_actual = (getcwd())
        self.nombre = nombre
        self.ruta_completa = self.ruta_actual + '/' + nombre
    
        ArchivoTxt.__init__(self, self.ruta_completa)


    def escribir_log(self, cadena_codigo, cadena):
        fecha = RangoFechas()
        fecha_act = fecha.fecha_actual()

        cadena_a_escribir = str(cadena_codigo) + ': '+str(cadena) + '-->' + str(fecha_act)
        self.comprobar_si_existe(cadena_a_escribir)

    def devolver_datos(self, codigo_solicitado):
        datos = list()
        conte = self.leer()

        for linea in conte:
            codigo = linea.split(':')[0]

            if codigo.upper() ==  codigo_solicitado.upper():

                datos.append(linea)

        return datos