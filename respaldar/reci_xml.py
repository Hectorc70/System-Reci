import sys

from modulos.rutas import unir_cadenas, crear_directorio
from modulos.archivo import Archivo
from modulos.log import Log

from modulos.pdf import ArchivoPdf
from respaldar.modelos.buscador import Buscador


class TimbreCop():
	def __init__(self, origen, periodo, anno, destino):
		self.carp_origen = origen
		self.periodo = periodo
		self.anno = anno

		self.carp_destino = destino

	def _formar_ruta_destino(self, ruta_orig):
		"""Forma la ruta de destino del archivo XML(TIMBRE)"""
		ruta_destino = ruta_orig.replace(self.carp_origen, self.carp_destino)

		return ruta_destino

	def copiado_archivos(self, ruta_archivo):
		"""Ejecuta el proceso de copiado de timbres XMLs
		de todas las nominas por periodo"""

		ruta_destino = self._formar_ruta_destino(ruta_archivo)

		tim = Archivo(ruta_archivo, ruta_destino, copiar=True)
		tim.comprobar_acciones()

		print('El proceso de copiado ah Terminado!!!')


class ReciboCop(ArchivoPdf):
	"""Clase que forma los datos
	y llama a los metodos correspondientes
	para el backup limpio de los recibos de nomina
	"""

	def __init__(self, orig_carpeta, ruta_orig, carpeta_dest):
		self.carpeta_orig = orig_carpeta
		self.carpeta_dest = carpeta_dest
		self.ruta_num = len(self.carpeta_orig.split('/'))
		self.ruta_origen = ruta_orig
		self.datos_nom = self._formar_ruta_destino()		
		self.patrones = ['CONTROL: [0123456789]{8}',
						'PERIODO:[0123456789]{1,2}/[0123456789]{4}'
						]

		ArchivoPdf.__init__(self, self.ruta_origen)

	def _formar_ruta_destino(self):
		"""
		retorna Ruta de destino(retorna la carpeta) de los recibos de nomina
		dependiendo del tipo de nomina
		"""
		ruta = self.ruta_origen.split('\\')
		nomina = ruta[self.ruta_num+1].split('_')[0]
		tipo_carpeta = ruta[-2]

		#ordinaria , complementaria, aguinaldos ordinaria
		if (tipo_carpeta == 'BASE' or 
			tipo_carpeta =='BASE4' or 
			tipo_carpeta =='CONFIANZA'
			):

			carpeta_prin =  ruta[:self.ruta_num+2]
			carpeta_destino = ruta[-2] + '_' + 'PDF'

			carpeta_prin.append(carpeta_destino)
			ruta_dest = unir_cadenas('\\', carpeta_prin)

			destino = ruta_dest.replace(
				self.carpeta_orig.replace('/','\\'), self.carpeta_dest.replace('/','\\'))
		
		elif nomina == 'JUBILADOS':		
			carpeta_prin =  ruta[:self.ruta_num+2]	
			ruta_dest = unir_cadenas('\\', carpeta_prin)		
			destino = ruta_dest.replace(
				self.carpeta_orig.replace('/','\\'), self.carpeta_dest.replace('/','\\'))

		else:
			carpeta_prin =  ruta[:self.ruta_num+3]
			ruta_dest = unir_cadenas('\\', carpeta_prin)
			destino = ruta_dest.replace(
				self.carpeta_orig.replace('/','\\'), self.carpeta_dest.replace('/','\\'))


		return [destino, nomina]

	def _almacenar_datos(self):
		"""retorna los metadatos de cada hoja del archivo 
		pdf formateados;
		[int:control, int:pagina,
		int:periodo, str:año]"""

		texto = list()
		datos_recibo = list()

		contenido_pdf = self.extraer_contenido()
		self.extraer_texto = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]

		for hoja, conte in contenido_pdf.items():
			for patron in self.patrones:
				buscador = Buscador(patron, conte[0])
				posiciones = buscador.buscar()

				if posiciones != None:
					texto_encontrado = self.extraer_texto(
						posiciones[0], posiciones[1], conte[0])

					texto.append(texto_encontrado)
			
			if texto:				
				control = int(texto[0].split(':')[1])
				periodo = int(texto[1].split(':')[1].split('/')[0])
				anno = str(texto[1].split(':')[1].split('/')[1])

				datos = [control, hoja, periodo, anno]               
				datos_recibo.append(datos)
				texto.clear()

			else:	
				log = Log('Log-copiado-Recibos.txt')
				error = 'ERROR:'
				mensaje = 'Hoja no leida' +'|'+ self.ruta_origen +'|'+'Hoja: '+str(hoja)
				log.escribir_log(error, mensaje)
				
			
				
				
				
				continue

		return datos_recibo

	def separar_en_recibos(self):
		"""Ejecuta la tarea de separar cada pagina
		en un archivo independiente"""


		contenido_paginas = self._almacenar_datos()
		if contenido_paginas:
			for contenido in contenido_paginas:
				control = contenido[0]
				pagina = contenido[1]
				per_anno = str(contenido[3]) + str("{:02d}".format(contenido[2]))
				nomina = self.datos_nom[1]
				
				nombre = unir_cadenas('_', [str(control), nomina, per_anno])
				crear_directorio(self.datos_nom[0])

				self.extraer_hoja(int(pagina), self.datos_nom[0], nombre)

			
		
