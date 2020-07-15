
from PyPDF2 import PdfFileReader


class ArchivoPdf():
			

	def leer_pdf(self, ruta):
		"""Lee archivo pdf"""		
		datos_recibos = list()

		for archivo in self.rutas_pdf:				
			self.lectura =PdfFileReader(archivo,'rb')
			paginas = self.lectura.numPages
			datos =  self.extraer_contenido(paginas, self.lectura, archivo, PATRONES)
			if len(datos) == 0:
				continue
			datos_recibos.append(datos)
		
		return datos_recibos
		
		
	
	def extraer_contenido(self, paginas, pdf_leido, ruta_archivo, patrones):
		"""Retorna el contenido por hoja del Archivo PDF,
			el numero de pagina, la ruta del archivo"""

		
		datos_pag = dict()

			
		for pagina in range(paginas):
			if pdf_leido.isEncrypted:
				self.lectura_encriptada(pdf_leido, pagina)				

			else:
				pagina_lect = pdf_leido.getPage(pagina)
				pdf_texto = pagina_lect.extractText()	
				pag = pagina+1

				buscar = self.buscar_texto(patrones, pdf_texto)
				if len(buscar) == 0:
					continue
				datos_pag[buscar[0]] = 	[pag, buscar[1], ruta_archivo]
		
		return datos_pag



			
		
									
	def lectura_encriptada(self, archivo, pag):
		pass




