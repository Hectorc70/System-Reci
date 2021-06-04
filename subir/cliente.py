import requests

from login.login import User

from modulos.log import Log
from modulos.rutas import unir_cadenas


import sys


class Cliente():

    def __init__(self, token):
        self.token = token
        self.base = 'http://10.1.2.209:8000'

    def enviar_empleado(self):
        pass

    def enviar_datos_recibo(self, datos_recibo):
        """"Envia datos para el registro de
        un recibo en la base de datos \n
        Parametros: Dict \n
        Salida: Respuesta del servidor"""

        uri = 'api/recibo/'
        ur_full = '{0}/{1}'.format(self.base, uri)
        headers = {'Authorization': 'Token {}'.format(self.token)}
        params = {
                "nombre_archivo": datos_recibo['archivo'],
                "ruta_archivo": datos_recibo['ruta'],
                "periodo": datos_recibo['periodo'],
                "tipo_nomina": datos_recibo['nomina'],
                "no_control": datos_recibo['control']
                }

        try:
            response = requests.post(ur_full, headers=headers, data=params)
            resp = response.json()

            if response.status_code == 200 or response.status_code == 201:
                response_token = resp['token']
                
                cadena = unir_cadenas('|', [str(response.status_code), 
                                            str(response_token),
                                            datos_recibo['ruta']
                                            ])
                log = Log('Log_Set_Recibos_Data.txt')
                log.escribir_log('OK', cadena)

            else:
                cadena = unir_cadenas('|', [str(response.status_code), 
                                            str(resp),
                                            datos_recibo['ruta']
                                            ])
                log = Log('Log_Set_Recibos_Data.txt')
                log.escribir_log('ERROR', cadena)

        
        except:

            cadena = unir_cadenas('|', ['0', 
                                        str(sys.exc_info()[1]),
                                        datos_recibo['ruta']
                                        ])
            
            log = Log('Log_Set_Recibos_Data.txt')
            log.escribir_log('ERROR', cadena)


            return [ 0, ]


