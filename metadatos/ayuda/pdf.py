
from PyPDF2 import PdfFileReader, PdfFileWriter


class ArchivoPdf():
	def __init__(self, ruta):

		self.ruta = ruta
		self.contenido = PdfFileReader(ruta,'rb')
		self.num_paginas = self.contenido.numPages

		
	
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


	def extraer_hoja(self, paginas, ruta_guardado, nombre_pdf):
        pdf_nuevo = PdfFileWriter()

		for pagina in paginas:
        	df_nuevo.addPage(self.contenido.getPage(int(pagina)))
        
        self.guardar_archivo(ruta_guardado, nombre_pdf, pdf_nuevo)

	def guardar_archivo(self, ruta, nombre_pdf, pdf):  
        nombre_archivo = ruta + '\\'+ nombre_pdf
        with open(nombre_archivo,'wb') as fp: 
            pdf.write(fp)

	