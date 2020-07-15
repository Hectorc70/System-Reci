from os.path import splitext

from metadatos.ayuda.pdf import ArchivoPdf
from metadatos.ayuda.rutas import Rutas, unir_cadenas, comprobar_rutas, abrir_archivo, dividir_cadena
from metadatos.ayuda.buscador import Buscador


PATRONES = ['CONTROL: [0123456789]{8}', 'PERIODO:[0123456789]{2}/[0123456789]{4}']
PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]




def rutas_recibos(ruta_recibos):
		rutas_pdf = dict()

		rutas = Rutas()
		rutas = rutas.recuperar_rutas(ruta_recibos, True)
		ruta_base_num = len(ruta_recibos.split('\\'))
		
		contador = 0
		for ruta in rutas:
			

			tipo_archivo = splitext(ruta[-1])[-1]
			if tipo_archivo == '.pdf':
				per = ruta[ruta_base_num+1].split('_')[0]
				anno = ruta[ruta_base_num+1].split('_')[1]
				nomina = ruta[ruta_base_num+2]				
				carp_reci = ruta[ruta_base_num+4]
				
				if per in PERIODOS and carp_reci == 'RECIBOS':
					contador = contador+1		
					ruta_completa = unir_cadenas('\\', ruta)
					rutas_pdf[str(contador)] = {'anno':anno, 'per':per,
												'nom':nomina, 'ruta':ruta_completa}
		
		return rutas_pdf

class ReciboNomina(ArchivoPdf):
	def __init__(self):
		ArchivoPdf.__init__(self)

	

	def buscar_datos(self, patrones, contenido_pdf):  
		"""retorna datos pasada por parametro""" 
		texto = list()     
		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	
		
		for patron in patrones:		
			buscador 		 = Buscador(patron, contenido_pdf)
			posiciones 		 = buscador.buscar()

			if len(posiciones) < 2:
				buscador 		 = Buscador('PERIODO:[0123456789]{1}/[0123456789]{4}', contenido_pdf)
				posiciones 		 = buscador.buscar()
				
				if len(posiciones) < 2:
					continue
					
			
			texto_encontrado = self.extraer_texto(posiciones[0], posiciones[1], contenido_pdf)
			
				
			

			texto.append(texto_encontrado)
				
			
		
		return texto
	
""" ruta = 'C:\\Users\\Hector\\Documents\\ARCHIVOS_PARA_PRUEBAS\\recibos'
reci = ReciboNomina()
rutas = reci.rutas_recibos(ruta)

print(rutas) """