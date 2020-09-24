from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas
from respaldar.modulos.archivo import Archivo

class ArchivosOrig:     
	
	def __init__(self, ruta, anno, periodo):

		self.ruta = ruta		
		self.periodo = periodo
		self.anno = anno
		self.ruta_com = self.formar_ruta()
		self.ruta_num  = len(self.ruta_com.split("/"))	
		self.rutas = Rutas()
		self.rutas_archivos = self.rutas.recuperar_rutas(self.ruta_com, True)
		self.datos_archivos = self.depurar_rutas()
	
	def formar_ruta(self):
		periodo_comp =  self.periodo + '_' + self.anno
		ruta = unir_cadenas('/', [self.ruta, periodo_comp])

		return ruta


	def depurar_rutas(self):
		"""Retorna solo archivos pdf y xml"""
		
		archivos_pdf = list()
		archivos_xml = list()

		for ruta in self.rutas_archivos:

			extencion_archivo = splitext(ruta[-1])

			if extencion_archivo[-1].lower() == '.pdf':   
				archivos_pdf.append(ruta)      
			elif extencion_archivo[-1].lower() == '.xml':
				archivos_xml.append(ruta)   		
		
		return [archivos_xml, archivos_pdf]


	def archivos_pdf(self):
		"""Retorna las rutas de los archivos de los
		recibos incluye jubilados"""
		recibos = list()
		
		for datos in self.datos_archivos[1]:
			if datos[self.ruta_num].upper().split('_')[0]=='JUBILADOS':				 
				datos_jub = self.archivos_pdf_jub(datos)
				if datos_jub:
					ruta = unir_cadenas('\\', datos_jub)
					datos_jub.append(ruta)
					recibos.append(datos_jub)

			elif (datos[self.ruta_num+2].upper() == 'RECIBOS' and
					datos[-2].upper() != 'MOD'):
				ruta = unir_cadenas('\\', datos)
				datos.append(ruta)
				recibos.append(datos)

		return recibos
	
	def archivos_pdf_jub(self, datos):
		if datos[self.ruta_num+1].upper() == 'RECIBOS':
			return datos



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

	