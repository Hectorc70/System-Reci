
from metadatos.ayuda.rutas import dividir_cadena
from metadatos.ayuda.pdf import ArchivoPdf



class Metadatos(ArchivoTxt):

	def __init__(self, archivo):
		super().__init__(archivo)

	def recuperar():
		
	def guardar(self):

	def leer(self):

		empleado = dict()			
		
		txt = ArchivoTxt(self.ruta_archivo)
		contenido_txt = txt.leer()

		for linea in contenido_txt:									
			linea_div = dividir_cadena('|', linea)
			if linea_div == '':
				continue
			if linea_div[-1] == '\n':
				linea_div.pop(-1)
					
			control = linea_div[0]
			periodo = linea_div[1]
			pagina = linea_div[2]
			ruta = linea_div[3]	
			
			llave = control + '|' + periodo + '|' + pagina
			empleado[llave] = ruta
		
		return empleado
			





		