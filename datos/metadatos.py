9


from modulos.rutas import unir_cadenas, Rutas
from datos.ayuda.recibo import NuevoReciNom
from modulos.bdatos import Bdatos
from datos.ayuda.log import Log

	

class ReciMetadatos(Bdatos):
	"""Clase que maneja los metadatos de los recibos 
	de nomina y se comunica con la base de datos"""

	def __init__(self, datos):
		self.host = '127.0.0.1'
		self.usuario = 'root'
		self.psw = ''
		self.nombre_bd = 'pruebas_recibos'

		self.datos = datos
		self.nombre_tbl = 'recibos'
		self.campos_col = 'control, periodo, anno, nomina, ruta'
		Bdatos.__init__(self, self.host, self.usuario,
						self.psw, self.nombre_bd)

	def _formar_datos(self):
		"""Formatea los datos 
		desde la ruta para el guardado del recibo en la base de datos
		"""

		control = self.datos[-1].split('\\')[-1].split('_')[0]
		self.datos.insert(0, control)
		control_format = "'"+str(control) + "'"
		per_format = "'"+str(self.datos[1])+"'"
		anno_format = "'"+self.datos[2]+"'"
		nomina = "'"+str(self.datos[3])+"'"
		ruta_format = "'"+self.datos[4].replace('\\','/')+"'"

		format_datos = unir_cadenas(',', [control_format, per_format,
										anno_format, nomina,
										ruta_format])

		return format_datos
	def guardar(self):
		"""invoca el metodo para insertar filas en la tabla de la base
				de datos"""


		datos = self._formar_datos()

		errores = self.insertar_filas(
			self.nombre_tbl, self.campos_col, datos)

		self.conexion.close()

	def devolver_datos(self, control, anno, periodos):
		"""Devuelve los recibos de los periodos
		pasados como parametro, del numero de control
		pasado como parametro, los parametros deben ser en
		string y los periodos como diccionarios"""

		periodo_recibos = dict()
		for anno, periodos in periodos.items():

			for periodo in periodos:
				campos = "id, control,periodo, anno, nomina,ruta"
				cond_control = "control = " + "'" + str(control) + "'"
				cond_anno = "anno = " + "'" + str(anno) + "'"
				cond_per = "periodo = " + "'" + str(periodo) + "'"
				condiciones = [cond_control, cond_anno, cond_per]
				condiciones = unir_cadenas(' AND ', condiciones)

				registros = self.consultar(self.nombre_tbl, condiciones, campos)
				datos = list(registros[0])
				
				periodo_recibos[datos[0]] = datos

		self.conexion.close()

		return periodo_recibos

	def extraer_recibos(self, registros, ruta_guardado):
		"""Consulta los registros y llama al metodo que extraer
				los recibos"""
		for registro in registros:

			nuevo_recibo = NuevoReciNom(ruta_guardado, registro)
			nuevo_recibo.guardar_recibo_buscado()

		

		self.conexion.close()

