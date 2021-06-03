from os.path import splitext

from modulos.rutas import unir_cadenas, Rutas
from modulos.archivo import Archivo

PERIODOS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
			'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'
			]



class RutaRecibo(Rutas):
	def __init__(self, ruta, in_anno, in_periodo, periodos=PERIODOS):
		self.ruta 			  = ruta
		self.in_periodo 	  = in_periodo
		self.in_anno 		  = in_anno
		self.periodos 		  = periodos
		
		self.ruta_base = self._formar_ruta_directorio()
		self.ruta_num = len(self.ruta.split('/'))
		Rutas.__init__(self)
	def _formar_ruta_directorio(self):
		ruta_base = self.ruta + '/' + self.in_periodo + '_' + self.in_anno
	
		return ruta_base
	
	
	def recuperar_periodo(self):
		"""Recupera los archivos de recibos por periodo
		si la propiedad de in_periodo se puso '01'...etc
		buscara en la carpeta de ese periodo"""

		rutas_archivos = list()
		

		rutas = self.recuperar_rutas(self.ruta_base, True)

		for ruta in rutas:			
			archivo      = splitext(ruta[-1])
			tipo_archivo = archivo[-1]


			if tipo_archivo == '.pdf':
				nombre_archivo = archivo[0]
				periodo    	   = ruta[self.ruta_num]
				nomina		   = ruta[self.ruta_num+1].split('_')[0]
				carpeta_nomina = ruta[self.ruta_num+1]

				if nomina == 'JUBILADOS':
					ruta_jub = unir_cadenas('/', ruta)
					datos_recibos_rutas=[nombre_archivo, periodo, carpeta_nomina, ruta_jub]

					rutas_archivos.append(datos_recibos_rutas)
				else:
					ruta_ord=self.__recuperar_recibos(
					ruta, carpeta_nomina, nombre_archivo, periodo)
					rutas_archivos.append(ruta_ord)


		return rutas_archivos

	def __recuperar_recibos(self, datos, nomina, nombre_recibo, periodo):
		
		try:
			carpeta	= datos[self.ruta_num+2].split('_')[1].upper()
			if carpeta == 'PDF':
				ruta=unir_cadenas('/', datos)
				datos_recibos_rutas=[nombre_recibo, periodo, nomina, ruta]
				return datos_recibos_rutas
		
		except:
			pass
		




class NuevoReciNom:		
	def __init__(self, ruta_guardado, datos_registro):		
		self.ruta_guardado = ruta_guardado
		self.datos_registro = datos_registro 
	
	def guardar_recibo_buscado(self):
		"""Llama a los metodos para la extraccion de un recibo
		ademas de crear una carpeta nueva con el nombre de numero de control
		"""

		control = str(self.datos_registro[0])
		anno_per = self.datos_registro[2]+self.datos_registro[3]
		datos_nombre = [control, str(self.datos_registro[1]), self.datos_registro[4], anno_per]
		nombre_archivo = unir_cadenas('_', datos_nombre) + '.pdf'
		
		ruta_guardado = unir_cadenas('/', [self.ruta_guardado, control, nombre_archivo])
		ruta_original = self.datos_registro[-1]

		recibo = Archivo(ruta_original, ruta_guardado, copiar=True)
		recibo.comprobar_acciones()
		
			