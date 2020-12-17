
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger



class ArchivoPdf():
	def __init__(self, ruta):

		self.ruta = ruta
		self.contenido =  PdfFileReader(self.ruta,'rb')
		self.num_paginas = self.contenido.numPages

	def extraer_contenido(self):
		"""Retorna el contenido por hoja del Archivo PDF,
			el dict{int:numero de pagina le suma 1  = str:contenido}"""

		
		datos_pag = dict()

			
		for pagina in range(self.num_paginas):
			if self.contenido.isEncrypted:
				self.lectura_encriptada(self.contenido, pagina)				

			else:
				pagina_lect = self.contenido.getPage(pagina)
				pdf_texto = pagina_lect.extractText()	
				pag = pagina+1

				datos_pag[pag] = 	[pdf_texto]
		
		return datos_pag

		
		
									
	def lectura_encriptada(self, archivo, pag):
		pass


	def extraer_hoja(self, pagina, ruta_guardado, nombre):
		"""Metodo que extrae la hoja indicada en un nuevo archivo.
		Parametros, int:pagina(pagina que se quiere extraer), 
		str:ruta_guardado(ruta de la carpeta donde se va a guardar),
		str:nombre(nombre de como se va a llamar el nuevo archivo debe
		ser sin el '.pdf')
		"""
			
		org_pag = self.contenido.getPage(pagina-1)

		pdf_salida = PdfFileWriter()
		pdf_salida.addPage(org_pag)		
			

		self.guardar_archivo(ruta_guardado, nombre, pdf_salida)
		
	def guardar_archivo(self, ruta, nombre_pdf, pdf):  
		nombre_archivo = ruta + '\\'+ nombre_pdf + '.pdf'
		with open(nombre_archivo,'wb') as fp: 
			pdf.write(fp)

		

