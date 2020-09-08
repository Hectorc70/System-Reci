
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger



class ArchivoPdf():
	def __init__(self, ruta=''):

		self.ruta = ruta
		self.contenido = self.contenido_pdf()[0]
		self.num_paginas = self.contenido_pdf()[1]

		
	def contenido_pdf(self):
		try:
			contenido = PdfFileReader(self.ruta,'rb')
			paginas = contenido.numPages
			return contenido, paginas
		except FileNotFoundError:
			return '', ''


	def extraer_contenido(self):
		"""Retorna el contenido por hoja del Archivo PDF,
			el numero de pagina, la ruta del archivo"""

		
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


	def extraer_hoja(self, archivo_org, pagina, ruta_guardado, nombre):
		
	
		
			original = PdfFileReader(archivo_org,'rb')
			org_pag = original.getPage(pagina)

			pdf_salida = PdfFileWriter()
			pdf_salida.addPage(org_pag)		
			

			self.guardar_archivo(ruta_guardado, nombre, pdf_salida)
		
	def guardar_archivo(self, ruta, nombre_pdf, pdf):  
		nombre_archivo = ruta + '\\'+ nombre_pdf + '.pdf'
		with open(nombre_archivo,'wb') as fp: 
			pdf.write(fp)

		

