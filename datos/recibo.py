from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas, crear_directorio
from modulos.pdf import ArchivoPdf
from datos.ayuda.buscador import Buscador

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





class ReciboNomina(ArchivoPdf):
	def __init__(self, ruta=''):
		self.ruta_pdf=ruta
		ArchivoPdf.__init__(self, self.ruta_pdf)
		self.patrones=['CONTROL: [0123456789]{8}',
									'PERIODO:[0123456789]{1,2}/[0123456789]{4}'
									]


	def almacenar_datos(self):
		"""retorna los metadatos formateados
		clave:control, periodo, año, pagina, ruta"""

		texto=list()
		datos_recibo=dict()

		contenido_pdf=self.extraer_contenido()
		self.extraer_texto=lambda pos_i, pos_f, texto: texto[pos_i:pos_f]


		for hoja, conte in contenido_pdf.items():
			for patron in self.patrones:
				buscador=Buscador(patron, conte[0])
				posiciones=buscador.buscar()

				if posiciones != None:
					texto_encontrado=self.extraer_texto(
					    posiciones[0], posiciones[1], conte[0])

					texto.append(texto_encontrado)


			if texto:
				control=int(texto[0].split(':')[1])
				periodo=int(texto[1].split(':')[1].split('/')[0])
				anno=str(texto[1].split(':')[1].split('/')[1])

				datos=[control, periodo, anno, hoja, self.ruta_pdf]
				datos_f=self.formatear_datos(datos)
				datos_recibo[datos_f[0]]=datos_f[1]
				texto.clear()
			else:
				print("--- Error al leer la hoja -----")
				continue

		return datos_recibo

	def formatear_datos(self, datos):
		"""Formatea los metadatos de los recibos
		para poder guardar en la base de datos
		"""


		control_format=str(datos[0])
		per_format="'"+str("{:02d}".format(datos[1]))+"'"
		anno_format="'"+datos[2]+"'"
		hoja_format=str(datos[3])
		ruta_format="'"+datos[-1]+"'"
		clave_format="'" + str(datos[0])+str("{:02d}".format(datos[1]))+datos[2]+hoja_format+"'"

		datos_f=[control_format,
					per_format, anno_format,
					hoja_format, ruta_format]
		datos_r=unir_cadenas(',', datos_f)



		return clave_format.replace("'", ''), datos_r

	def guardar_recibos_extraidos(self, nombre_pdf, ruta_guardado, datos):
		"""Llama a los metodos para la extraccion de un recibo
		ademas de crear una carpeta nueva con el nombre de numero de control
		antes de"""


		ruta_guardado=ruta_guardado + '/' + str(nombre_pdf)
		crear_directorio(ruta_guardado)

		for dato in datos:

			nombre_archivo=dato[-1].split('/')[-1].split('.')[0]
			nombre=[str(nombre_pdf), str(dato[0]), nombre_archivo]
			nombre=unir_cadenas('_', nombre)
			self.extraer_hoja(dato[2], ruta_guardado, nombre)
