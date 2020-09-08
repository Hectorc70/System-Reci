import pymysql


class Bdatos:
	def __init__(self, host, usuario, psword, nombre_bd):       
		self.host    = host
		self.usuario = usuario
		self.psw     = psword
		self.nombre_bd = nombre_bd
		self.conexion = pymysql.connect(self.host, self.usuario, self.psw, self.nombre_bd)
		self.cursor    = self.conexion.cursor()
		self.errores_guardado = dict()
	
	
	def crear_tabla(self, tabla):
		orden = "CREATE TABLE {}.{}(id INT AUTO_INCREMENT,control INT(8) NOT NULL, \
				periodo VARCHAR(2) NOT NULL, anno VARCHAR(4) NOT NULL, \
				pagina INT(4) NOT NULL, ruta VARCHAR(300) NOT NULL,\
				PRIMARY KEY(id), UNIQUE KEY(id))".format(self.nombre_bd, tabla)


		self.cursor.execute(orden)
		self.conexion.commit()
		

	def insertar_filas(self, nombre_tabla, campos, datos):
		
		try:
			tabla = "SELECT 1 FROM {} LIMIT 1".format(nombre_tabla)
			self.cursor.execute(tabla)

		except pymysql.err.ProgrammingError:
			print("No existe la tabla pero se procedera a crearla")
			self.crear_tabla(nombre_tabla)			
		
		
		try:
			orden = "INSERT INTO {}({}) \
			VALUES({})".format(nombre_tabla, campos, datos) 
			self.cursor.execute(orden)
			self.conexion.commit()			
					
		except pymysql.err.IntegrityError:
			self.errores_guardado[datos.split(',')[0]] = datos
			print("WARNING: Ya Existe el registro: {} No se Pudo Guardar".format(datos.split(',')[0]))
			pass

		
		
		return self.errores_guardado		
		
			
			
	
	def consultar(self,nombre_tabla, control, anno, periodo):
		try:
			tabla = "SELECT pagina, ruta FROM {} LIMIT 1".format(nombre_tabla)
			self.cursor.execute(tabla)

		except pymysql.err.ProgrammingError:
			print("No existen datos de este año")		
			pass
		
		orden = "SELECT id, pagina, ruta FROM recibosnomina.recibos\
				WHERE control={} and anno = {} and periodo={}".format(control, anno, periodo)
				

		self.cursor.execute(orden)
		
		registro = self.cursor.fetchall()
		return registro

		
campos = 'id, control, periodo, anno, pagina, ruta'
datos = "'31821201202010', 318212, '01', '2020', 10, 'C:/pruebas/prueba.pdf'"

""" recibos = Bdatos(host, usuario, psword, bd_nombre)
recibos.insertar_filas('r2020', datos, campos) """