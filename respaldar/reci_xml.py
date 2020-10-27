from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas, crear_directorio
from respaldar.originales import ArchivoTimbre
from respaldar.modelos.archivo import Archivo


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