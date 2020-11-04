from os.path import splitext

from modulos.rutas import unir_cadenas, Rutas
from modulos.archivo import Archivo

PERIODOS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
			'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'
			]



class RutaRecibo(Rutas):
	def __init__(self, ruta, in_anno, in_periodo, periodos=PERIODOS):
		self.ruta = ruta
		self.in_periodo = in_periodo
		self.in_anno = in_anno
		self.periodos = periodos
		
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
			archivo=splitext(ruta[-1])
			tipo_archivo=archivo[-1]


			if tipo_archivo == '.pdf':
				nombre_archivo=archivo[0]
				periodo=nombre_archivo.split('_')[-1][-2:]
				anno=nombre_archivo.split('_')[-1][:4]
				nomina=nombre_archivo.split('_')[1]

				if nomina == 'ORDINARIA':
					ruta_ord=self._recuperar_recibos_ordinaria(
					    ruta, nomina, periodo, anno)
					rutas_archivos.append(ruta_ord)

				elif nomina == 'JUBILADOS':
					ruta_jub = unir_cadenas('\\', ruta)
					datos_recibos_rutas=[periodo, anno, nomina, ruta_jub]

					rutas_archivos.append(datos_recibos_rutas)
				else:
					ruta_esp=self._recuperar_recibos_especiales(
					    ruta, nomina, periodo, anno)
					rutas_archivos.append(ruta_esp)


		return rutas_archivos

	def _recuperar_recibos_ordinaria(self, datos, nomina, periodo, anno):
		rutas_recibos=list()
		carpeta=datos[self.ruta_num+2].upper()

		if carpeta.split('_')[-1] == 'PDF':
			ruta=unir_cadenas('\\', datos)
			datos_recibos_rutas=[periodo, anno, nomina, ruta]
		

			return datos_recibos_rutas


	def _recuperar_recibos_especiales(self, datos, nomina, periodo, anno):
		
		carpeta=datos[self.ruta_num+2].upper()

		if carpeta == 'PDF':
			ruta=unir_cadenas('\\', datos)
			datos_recibos_rutas=[periodo, anno, nomina, ruta]		

			return datos_recibos_rutas





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
		
			