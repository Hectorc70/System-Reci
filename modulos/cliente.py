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

		datos = [self.accion, self.usuario, self.psw, self.bd, self.tabla]

		datos = unir_cadenas('_', datos)
		
		return datos

	def conectar(self):		
			self.cliente.connect((self.ip, self.puerto))			
			datos = self._formatear_datos()
			
			self.cliente.send(datos.encode())
			print('CONECTADO CON EXITO')
			respuesta = self.cliente.recv(1024).decode()
			print(respuesta)
			self.cliente.close()
			return True

	