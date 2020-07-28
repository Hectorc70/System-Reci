from os.path import splitext

from metadatos.ayuda.rutas import Rutas, unir_cadenas, comprobar_rutas, abrir_archivo, dividir_cadena
from metadatos.ayuda.pdf import ArchivoPdf
from metadatos.ayuda.buscador import Buscador

PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]



def rutas_recibos(ruta_recibos, anno, periodo='0'):
		rutas_pdf = dict()		
		rutas = Rutas()
		if periodo !='':
			rutas_recibos = rutas_recibos + '/' + periodo+'_'+anno 
		
		rutas = rutas.recuperar_rutas(ruta_recibos, True)
		ruta_base_num = len(ruta_recibos.split('/'))
		
		contador = 0
		for ruta in rutas:			

			tipo_archivo = splitext(ruta[-1])[-1]
			if tipo_archivo == '.pdf':
				per = ruta[ruta_base_num].split('_')[0]
				anno = ruta[ruta_base_num].split('_')[1]
				nomina = ruta[ruta_base_num+1]				
				carp_reci = ruta[ruta_base_num+3]				
				
				if per == periodo and carp_reci == 'RECIBOS':
					contador = contador+1		
					ruta_completa = unir_cadenas('/', ruta)
					rutas_pdf[str(contador)] = {'anno':anno, 'per':per,
												'nom':nomina, 'ruta':ruta_completa}
				

		return rutas_pdf

class ReciboNomina(ArchivoPdf):
	def __init__(self, ruta):
		self.ruta_pdf = ruta
		ArchivoPdf.__init__(self, self.ruta_pdf)
		self.patrones = PATRONES = ['CONTROL: [0123456789]{8}', 
									'PERIODO:[0123456789]{1,2}/[0123456789]{4}'
									]	


	def formateo_datos(self):  
		"""retorna los metadatos formateados
		clave:control, periodo, año, pagina, ruta""" 

		texto = list()
		datos_recibo = dict()
		
		contenido_pdf = self.extraer_contenido()
		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	
		
		
		for hoja, conte in contenido_pdf.items():
			for patron in self.patrones:		
				buscador 		 = Buscador(patron, conte[0])
				posiciones 		 = buscador.buscar()

				texto_encontrado = self.extraer_texto(posiciones[0], posiciones[1], conte[0])	

				texto.append(texto_encontrado)			
			
			control = 	int(texto[0].split(':')[1])
			periodo = 	int(texto[1].split(':')[1].split('/')[0])		
			anno    =   str(texto[1].split(':')[1].split('/')[1])

			datos = [control, periodo, anno, hoja, self.ruta_pdf]
			datos_f = self.formatear_datos(datos)
			datos_recibo[datos_f[0]] = datos_f[1]
			texto.clear()
		
		return datos_recibo

	def formatear_datos(self, datos):
		"""Formatea los metadatos de los recibos 
		para poder guardar en la base de datos
		"""


		control_format = str(datos[0])
		per_format = "'"+str("{:02d}".format(datos[1]))+"'"
		anno_format = "'"+datos[2]+"'"
		hoja_format = str(datos[3])
		ruta_format = "'"+datos[-1]+"'" 
		clave_format = "'"+str(datos[0])+str("{:02d}".format(datos[1]))+datos[2]+hoja_format+"'"
		
		datos_f = [clave_format, control_format,
					per_format, anno_format, 
					hoja_format, ruta_format]
		datos_r = unir_cadenas(',',datos_f)
		
		

		return clave_format.replace("'",''), datos_r


""" ruta = 'C:\\Users\\Hector\\Documents\\ARCHIVOS_PARA_PRUEBAS\\recibos'
reci = ReciboNomina()
rutas = reci.rutas_recibos(ruta)

print(rutas) """