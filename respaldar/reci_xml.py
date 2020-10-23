from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas
from respaldar.modulos.archivo import Archivo


class ArchivoRecibo(Archivo):
	"""Clase que forma los datos
	y llama a los metodos correspondientes
	para el backup limpio de los recibos de nomina 
	"""
	def __init__(self, orig_carpeta, ruta_orig, carpeta_dest, nombre, copiar):
		self.carpeta_orig = orig_carpeta.replace('/', '\\')	
		self.carpeta_dest = carpeta_dest.replace('/', '\\')	
		
		self.origen =  ruta_orig
		self.destino = self.formar_ruta_destino()	
		
		self.nombre = nombre
		self.copiar = copiar
		Archivo.__init__(self, self.origen, self.destino, self.nombre,  self.copiar)
		
	def formar_ruta_destino(self):
		destino = self.origen.replace(self.carpeta_orig, self.carpeta_dest)

		
		
		return destino

