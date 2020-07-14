import os.path as path 



class ArchivoTxt:
	"""Trabaja con archivos txt"""

	def __init__(self, archivo):
		
		self.ruta_archivo = archivo	

	def comprobar_si_existe(self, texto):	
		
		if path.exists(self.ruta_archivo):
			self.escribir(texto)
		else:
			self.crear(texto)
		

	def escribir(self, datos):
		
		archivo_r = open(self.ruta_archivo, "a")
		archivo_r.write(datos + '\n'  )
		
		archivo_r.close() 
		
		print("leido y escrita la INFO")

	def leer(self, lineas = True):

		if lineas:
			archivo_r = open(self.ruta_archivo, "r")
			contenido_txt = archivo_r.readlines()
			archivo_r.close() 
		else:
			archivo_r = open(self.ruta_archivo, "r")
			contenido_txt = archivo_r.read()
			archivo_r.close() 

		return contenido_txt
	
	def crear(self, datos):

		archivo_r = open(self.ruta_archivo, "w")
		archivo_r.write('\n' + datos)


