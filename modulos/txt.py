import os.path as path 



class ArchivoTxt:
	"""Trabaja con archivos txt"""

	def __init__(self, archivo):
		
		self.ruta_archivo = archivo	

	def comprobar_si_existe(self, texto, escribir_txt =True):	
		
		if path.exists(self.ruta_archivo):
			self.escribir(texto)
		else:
			self.crear(texto, escribir_txt)
		

	def escribir(self, datos):
		
		archivo_r = open(self.ruta_archivo, "a")
		archivo_r.write(datos + '\n')
		
		archivo_r.close() 
		

	def leer(self, lineas = True):
		conte_txt = list()
		if lineas:
			archivo_r = open(self.ruta_archivo, "r")
			contenido_txt = archivo_r.readlines()
			archivo_r.close() 
		else:
			archivo_r = open(self.ruta_archivo, "r")
			contenido_txt = archivo_r.read()
			archivo_r.close() 

		for contenido in contenido_txt:
			contenido = contenido.replace('\n','')
			conte_txt.append(contenido)
		
		return conte_txt
	
	def crear(self, datos, escribir):

		archivo_r = open(self.ruta_archivo, "w")
		if escribir:
			self.escribir(datos)

		archivo_r.close()

