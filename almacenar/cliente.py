import socket

from modulos.rutas import unir_cadenas


class Cliente:

	def __init__(self, ip, puerto, usuario, psw, bd, tabla, accion):
		self.ip = ip
		self.puerto = puerto
		self.cliente = socket.socket()
		self.usuario  = usuario
		self.psw 	  = psw
		self.bd 	  = bd	
		self.tabla 	  = tabla
		self.accion   = accion
	

	def _formatear_datos(self):
		datos_conexion = unir_cadenas(',', [self.usuario, self.psw, self.bd, self.tabla])
		datos = [self.accion, datos_conexion]

		datos = unir_cadenas('|', datos)
		
		return datos

	def conectar(self):		
			conexion = self.cliente.connect((self.ip, self.puerto))
				
			print('CONECTADO CON EXITO')		
			datos = self._formatear_datos()	
					
			self.cliente.send(datos.encode())
				
			respuesta = self.cliente.recv(1024).decode()
			print(respuesta)
			self.cliente.close()
			return True

	