
from metadatos.ayuda.rutas import dividir_cadena, unir_cadenas
from metadatos.recibo import ReciboNomina
from metadatos.ayuda.bdatos import Bdatos
from metadatos.ayuda.log import Log




class ReciMetadatos(Bdatos):
	"""Clase que maneja los metadatos de los recibos 
	de nomina y se comunica con la base de datos"""

	def __init__(self, metadatos, anno):
		self.host      = '127.0.0.1'
		self.usuario   = 'root'
		self.psw       = '' 
		self.nombre_bd ='recibosnomina'

		self.datos     = metadatos
		self.nombre_tbl = 'r'+str(anno)
		self.campos_col = 'id, control, periodo, anno, pagina, ruta'
		Bdatos.__init__(self,self.host, self.usuario, self.psw, self.nombre_bd)
	

	def guardar(self):
		"""invoca el metodo para insertar filas en la tabla de la base
			de datos
			su parametro deben ser un diccionarios"""
		
		for clave, datos in self.datos.items():						
			self.errores_guardado.clear()			
			errores = self.insertar_filas(self.nombre_tbl, self.campos_col, datos)

			if errores:
				log = Log('log.txt', 'C:\log_recibos_metadatos')
				log.guardar_datos(self.errores_guardado, '|')
			else: 
				continue
		
		self.conexion.close()


	

	def leer(self, control, fecha_ini ,fecha_final):

		pass






