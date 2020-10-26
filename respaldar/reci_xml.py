from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas, crear_directorio
from respaldar.originales import ArchivoTimbre
from respaldar.modelos.archivo import Archivo


class TimbreCop(ArchivoTimbre):
	def __init__(self, ruta, periodo, anno, destino):	
		self.ruta = ruta		
		self.periodo = periodo
		self.anno = anno

		self.ruta_dest = destino
		

		ArchivoTimbre.__init__(self, self.ruta, self.periodo, self.anno)
		
	def _formar_ruta_destino(self, ruta_orig):
		"""Forma la ruta de destino del archivo XML(TIMBRE)"""
		ruta = unir_cadenas('/', ruta_orig)
		ruta_destino = ruta.replace(self.ruta, self.ruta_dest)
		
		
		return ruta_destino

	def copiado_archivos(self):
		"""Ejecuta el proceso de copiado de timbres XMLs
		de todas las nominas por periodo"""
		
		timbres = self.recuperar_timbres()
		
		for timbre in timbres:
			ruta_destino = self._formar_ruta_destino(timbre)
			ruta_orig = unir_cadenas('/', timbre)
			tim = Archivo(ruta_orig, ruta_destino, copiar=True)
			tim.comprobar_acciones()
		
		
		print('El proceso de copiado ah Terminado!!!')
	


class Recibo(Archivo):
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

	def recibos(self):
		pass