import socket

from modulos.rutas import unir_cadenas


class Cliente:

	def __init__(self, ip, puerto, usuario, psw, bd, tabla):
		self.ip = ip
		self.puerto = puerto
		self.cliente = socket.socket()
		self.usuario  = usuario
		self.psw 	  = psw
		self.bd 	  = bd	
		self.tabla 	  = tabla
		

		self._conectar()

	def _formatear_datos(self, instruccion):
		datos_conexion = unir_cadenas(',', [self.usuario, self.psw, self.bd, self.tabla])
		datos = [instruccion, datos_conexion]

		datos = unir_cadenas('|', datos)
		
		return datos

	def _conectar(self):		
			self.cliente.connect((self.ip, self.puerto))
				
			print('CONECTADO CON EXITO')		
			

	def enviar_datos(self, instruccion):
		"""RETORNA DATOS DEL
		SERVIDOR"""

		datos = self._formatear_datos(instruccion)	
					
		self.cliente.send(datos.encode())				
		respuesta = self.cliente.recv(1024).decode()
		
		return respuesta

	def cerrar_conexion(self):
		self.cliente.close()
		
