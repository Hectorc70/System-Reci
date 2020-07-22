
from metadatos.ayuda.pdf import ArchivoPdf
from metadatos.ayuda.buscador import Buscador





def rutas_recibos(directorio):
		rutas_pdf = dict()
		ruta_recibos = directorio.replace('/', '\\')
		rutas = Rutas()
		rutas = rutas.recuperar_rutas(ruta_recibos, True)
		ruta_base_num = len(ruta_recibos.split('\\'))
		
		contador = 0
		for ruta in rutas:
			

			tipo_archivo = splitext(ruta[-1])[-1]
			if tipo_archivo == '.pdf':
				per = ruta[ruta_base_num].split('_')[0]
				anno = ruta[ruta_base_num].split('_')[1]
				nomina = ruta[ruta_base_num+1]				
				carp_reci = ruta[ruta_base_num+3]
				
				if per in PERIODOS and carp_reci == 'RECIBOS':
					contador = contador+1		
					ruta_completa = unir_cadenas('\\', ruta)
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

	def buscar_datos(self):  
		"""retorna datos pasada por parametro""" 

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
			per_format = str("{:02d}".format(periodo))
			anno    =   str(texto[1].split(':')[1].split('/')[1])		
			
			clave =  str(control)+per_format+anno+str(hoja)
			datos_recibo[clave] = [control,per_format,anno,hoja,self.ruta_pdf]
			texto.clear()
		
		return datos_recibo
	




""" ruta = 'C:\\Users\\Hector\\Documents\\ARCHIVOS_PARA_PRUEBAS\\recibos'
reci = ReciboNomina()
rutas = reci.rutas_recibos(ruta)

print(rutas) """