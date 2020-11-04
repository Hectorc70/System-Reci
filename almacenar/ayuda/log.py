import datetime

from datos.ayuda.txt import ArchivoTxt
from modulos.rutas import unir_cadenas





class Log(ArchivoTxt):
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.ruta_c = self.ubicacion + '/'+self.nombre
        ArchivoTxt.__init__(self, self.ruta_c)
    
    def guardar_datos(self, datos, separador):
        """Guarda los datos pasados por parametro
        deben ser en diccionarios ejemplo
        'error':["dato1", datos2, 'dato3', 'error']"""
        
        fecha = datetime.datetime.now()
        for clave, datos in datos.items():
            datos = datos + '|' + fecha.strftime("%Y-%m-%d %H:%M.%S")
            self.comprobar_si_existe(datos)




