
from os.path import splitext

from PyPDF2 import PdfFileReader


from metadatos.ayuda.rutas import Rutas, unir_cadenas, comprobar_rutas, abrir_archivo, dividir_cadena
from metadatos.ayuda.buscador import Buscador
from metadatos.ayuda.txt import ArchivoTxt


PATRONES = ['CONTROL: [0123456789]{8}', 'PERIODO:[0123456789]{2}/[0123456789]{4}']
PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
            '12','13','14','15','16','17','18','19','20','21','22','23','24'
			]

def depurar_rutas(ruta_archivo_pdf):
	rutas_pdf = list()
	rutas = Rutas()
	rutas = rutas.recuperar_rutas(ruta_archivo_pdf, True)
	ruta_base_num = len(ruta_archivo_pdf.split('\\'))
	

	for ruta in rutas:

		tipo_archivo = splitext(ruta[-1])[-1]
		if tipo_archivo == '.pdf':
			per = ruta[ruta_base_num].split('_')[0]
			carp_reci = ruta[ruta_base_num+3]

			if per in PERIODOS and carp_reci == 'RECIBOS':		
				ruta_completa = unir_cadenas('\\', ruta)
				rutas_pdf.append(ruta_completa)
	
	return rutas_pdf


class ArchivoPdfLectura():

	def __init__(self, rutas):	
		
		self.rutas_pdf = depurar_rutas(rutas)
		
	

		

	def leer_pdf(self):
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


	def buscar_texto(self, patrones, contenido_pdf):
		"""retorna la palabra pasada por parametro"""
		
		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	

		texto = list()
	
		for patron in patrones:
			
				
			buscador 		 = Buscador(patron, contenido_pdf)
			posiciones 		 = buscador.buscar()

			if len(posiciones) < 2:
				buscador 		 = Buscador('PERIODO:[0123456789]{1}/[0123456789]{4}', contenido_pdf)
				posiciones 		 = buscador.buscar()
				
				if len(posiciones) < 2:
					continue
					
			
			texto_encontrado = self.extraer_texto(posiciones[0], posiciones[1], contenido_pdf)
			
				
			

			texto.append(texto_encontrado)
				
			
		
		return texto
	


			
		
									
	def lectura_encriptada(self, archivo, pag):
		pass




