
from modulos.rutas import unir_cadenas, Rutas
from datos.recibo import ReciboNomina
from modulos.bdatos import Bdatos
from datos.ayuda.log import Log




class ReciMetadatos(Bdatos):
	"""Clase que maneja los metadatos de los recibos 
	de nomina y se comunica con la base de datos"""

	def __init__(self, metadatos, anno):
		self.host      = '127.0.0.1'
		self.usuario   = 'root'
		self.psw       = ''
		self.nombre_bd ='pruebas_recibos'

		self.datos     = metadatos
		self.nombre_tbl = 'recibos'
		self.campos_col = 'control, periodo, anno, ruta'
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


	

	def devolver_datos(self, control, anno, periodos):
		"""Devuelve los recibos de los periodos
		pasados como parametro, del numero de control
		pasado como parametro, los parametros deben ser en
		string y los periodos como diccionarios"""

		periodo_recibos = dict()
		for anno, periodos in periodos.items():

			for periodo in periodos:
				campos = "id, periodo, anno, ruta"
				cond_control = "control = " + "'" + str(control) + "'"
				cond_anno = "anno = " + "'" + str(anno) +"'"
				cond_per = "periodo = " + "'" + str(periodo) + "'"
				condiciones = [cond_control, cond_anno, cond_per]
				condiciones = unir_cadenas(' AND ', condiciones)
				
				registros = self.consultar(self.nombre_tbl, condiciones ,campos)
				
				for registro in registros:
					nombre_archivo = registro[-1].split('/')[-1].split('.')[0] 
					registro = list(registro)
					registro.append(nombre_archivo)
					periodo_recibos[str(registro[0])] = registro
				
		
		self.conexion.close()		
		
		return periodo_recibos


	def consultar_extraer_recibos(self, id_registros, ruta_guardado):
		"""Consulta los registros y llama al metodo que extraer
			los recibos"""
		for id_registro in id_registros:
			campos = "id, control, pagina, ruta"
			condiciones = "id = " + "'"+ id_registro + "'"
			registro = self.consultar(self.nombre_tbl, condiciones ,campos)

			recibo = ReciboNomina(registro[0][-1])
			recibo.guardar_recibos_extraidos(registro[0][1], ruta_guardado, registro)

		self.conexion.close()