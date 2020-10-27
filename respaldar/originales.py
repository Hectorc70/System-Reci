
from os.path import splitext

from modulos.rutas import Rutas, unir_cadenas

class ArchivosOrig:     
	"""Clase que recupera los
	archivos PDF Y XML"""
	def __init__(self, ruta, periodo, anno):

		self.ruta = ruta		
		self.periodo = periodo
		self.anno = anno
		self.ruta_com = self._formar_ruta()
		self.ruta_num  = len(self.ruta_com.split("/"))	
		self.rutas = Rutas()
		self.rutas_archivos = self.rutas.recuperar_rutas(self.ruta_com, True)
		
	
	def _formar_ruta(self):
		periodo_comp =  self.periodo + '_' + self.anno
		ruta = unir_cadenas('/', [self.ruta, periodo_comp])

		return ruta


	def depurar_rutas(self):

		"""Retorna solo archivos pdf y xml"""
		
		archivos_pdf = list()
		archivos_xml = list()

		for ruta in self.rutas_archivos:

			extencion_archivo = splitext(ruta[-1])

			if extencion_archivo[-1].lower() == '.pdf':				
				archivos_pdf.append(ruta)  

			elif extencion_archivo[-1].lower() == '.xml':
				archivos_xml.append(ruta)   		
		
		return archivos_pdf, archivos_xml


class ArchivoTimbre(ArchivosOrig):
	"""Clase que depura archivos dejando solo
	los timbres de todas las nominas"""
	def __init__(self, origen, periodo, anno):	
		self.carpeta_origen = origen		
		self.periodo = periodo
		self.anno = anno
		ArchivosOrig.__init__(self, self.carpeta_origen, self.periodo, self.anno)
	
	
	def recuperar_timbres(self):
		archivos = self.depurar_rutas()
		timbres = list()

		for datos in archivos[1]:
			
			if len(datos[-1].split('_')[0]) == 8:				
				nomina = datos[self.ruta_num].split('_')[0]
				periodo_anno = datos[self.ruta_num-1]	
				ruta = unir_cadenas('/', datos)
				datos = [periodo_anno, nomina , ruta]
				timbres.append(datos)

		
		return timbres
			


class ArchivoRecibo(ArchivosOrig):
	"""Clase que depura y devuelve solo las 
		rutas de los recibos de nomina en PDF
		de todas las nominas"""
	def __init__(self, ruta, anno, periodo):

		self.ruta = ruta		
		self.periodo = periodo
		self.anno = anno
		ArchivosOrig.__init__(self, self.ruta, self.periodo, self.anno)

	def recuperar_recibos(self):
		"""Retorna las rutas de los archivos de los
		recibos incluye jubilados"""
		
		
		recibos = list()
		
		rutas = self.depurar_rutas()

		for datos_rutas in rutas[0]:		

			nomina = datos_rutas[self.ruta_num].upper().split('_')[0]

			if nomina=='ORDINARIA' or 'COMPLEMENTARIA':
				reci_ord = dict()
				ruta_reci = self.recibos_ordinaria(datos_rutas)
				if ruta_reci:
					reci_ord[nomina] = ruta_reci
					recibos.append(reci_ord)
			elif nomina=='JUBILADOS':
				reci_jub = dict()
				ruta_reci = self.recibos_jubilados(datos_rutas)
				
				if ruta_reci:
					reci_jub[nomina] = ruta_reci
					recibos.append(reci_jub)
					
			elif nomina != 'REPORTES':
				carpeta = datos_rutas[self.ruta_num+2].upper()
				if carpeta == 'RECIBOS':
					ruta = unir_cadenas('\\', datos_rutas)
					print(ruta)

	def recibos_ordinaria(self, datos):
		recibos = dict()
		

		carpeta = datos[self.ruta_num+2].upper()

		if carpeta.upper() == 'RECIBOS':
			ruta = unir_cadenas('\\', datos)
			t_nom =  datos[-2]

			if t_nom == 'BASE':
				recibos['R-BASE'] = ruta
			elif t_nom == 'BASE4':
				recibos['R-BASE4'] = ruta
			elif t_nom == 'CONFIANZA':
				recibos['R-CONFIANZA'] = ruta			
		else:
			pass

		return recibos
		


	def recibos_jubilados(self, datos):				
		if datos[self.ruta_num+1].upper() == 'RECIBOS':
			ruta = unir_cadenas('\\', datos)
			return ruta




""" ruta = 'Y:/CFDI_2020/CFDI_NOMINA_2020'
origen = Timbre(ruta, '08',  '2020')
origen.recuperar_timbres() """