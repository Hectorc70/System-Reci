from almacenar.cliente import Cliente

from modulos.rutas import unir_cadenas

class RegistroRecibo:
	"""
	Clase que maneja registros(recibos de nomina)
	"""

	def __init__(self, control, periodo, anno, t_nomina, ruta_archivo):
		self.control = control
		self.periodo = periodo
		self.anno = anno
		self.t_nomina = t_nomina
		self.ruta_archivo = ruta_archivo

		self.campos = "control, periodo, anno, nomina, ruta"

	def guardar(self):
		"""Crea la cadena que se envia
		hacia el servidor para insertar 
		datos en la base de datos
		devuelve  una cadena de texto"""


		self.control = "'"+str(self.control)+"'"
		self.periodo = "'"+str(self.periodo)+"'"
		self.anno = "'"+str(self.anno)+"'"
		self.t_nomina = "'"+str(self.t_nomina)+"'"
		self.ruta_archivo = "'"+str(self.ruta_archivo)+"'"

		datos = unir_cadenas(',', [self.control, self.periodo, 
							self.anno, self.t_nomina, self.ruta_archivo])
		
		accion = "INSERTAR:" + self.campos + '|' + datos
		
		return accion
		

	def consultar(self):
		pass

	def modificar(self):
		pass




class RegistroEmpleado():
	def __init__(self, control, nombre, apellidop, apellidom):
		self.control = control				
		self.nombre = nombre
		self.apellidop = apellidop
		self.apellidom = apellidom
		self.campos = "NoControl, Nombre, ApellidoP, ApellidoM"




	def guardar(self):
		"""Crea la cadena que se envia
		hacia el servidor para insertar 
		datos en la base de datos
		devuelve  una cadena de texto"""


		self.control = "'"+str(self.control)+"'"
		self.nombre = "'"+str(self.nombre)+"'"
		self.apellidop = "'"+str(self.apellidop)+"'"
		self.apellidom = "'"+str(self.apellidom)+"'"	

		datos = unir_cadenas(',', [self.control, self.nombre, 
							self.apellidop, self.apellidom])
		
		accion = "INSERTAR:" + self.campos + '|' + datos
		
		return accion


	def consultar(self):
		pass

	def modificar(self):
		pass