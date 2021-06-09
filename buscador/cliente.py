import requests
import sys

from modulos.rutas import unir_cadenas
from modulos.log import Log




class ClienteBuscador():

    def __init__(self, token):
        self.token = token
        self.base = 'http://10.1.2.209:8000'

    def recuperar_control(self, nombre, ape_p, ape_m):
        datos_busqueda = unir_cadenas('_',[nombre, ape_p, ape_m])
        
        uri = 'api/empleado/{}/{}/{}'.format(nombre.upper(),
                                            ape_p.upper(),
                                            ape_m.upper(),)
        ur_full = '{0}/{1}'.format(self.base, uri)

        headers = {'Authorization': 'Token {}'.format(self.token)}

        try:
            response = requests.get(ur_full, headers=headers)
            resp = response.json()

            if response.status_code == 200:
                cadena = unir_cadenas('|', [str(response.status_code), 
                                            datos_busqueda
                                            ])

                log = Log('Log_Buscador_Recibos.txt')
                log.escribir_log('OK', cadena)

                return resp
            
            
            else:

                cadena = unir_cadenas('|', [str(response.status_code), 
                                            str(resp),
                                            datos_busqueda
                                            ])
                log = Log('Log_Buscador_Recibos.txt')
                log.escribir_log('ERROR', cadena)


        except:
            cadena = unir_cadenas('|', ['0', 
                                        str(sys.exc_info()[1]),
                                        datos_busqueda
                                        ])
            
            log = Log('Log_Buscador_Recibos.txt')
            log.escribir_log('ERROR', cadena)


            return [ 0, '']

    def recuperar_recibo(self, id_recibo):
        
        uri = 'api/recibo-file/{}'.format(id_recibo)
        ur_full = '{0}/{1}'.format(self.base, uri)

        headers = {'Authorization': 'Token {}'.format(self.token)}

        try:
            response = requests.get(ur_full, headers=headers)
            
            if response.status_code == 200:
                resp = response.text
                return [response.status_code, str(resp)]
            
            else:
                resp = response.content
                return [response.status_code, str(resp)]

        except:

            return [ 0, '']


    def recuperar_datos_recibo(self, control, periodo):
        datos_busqueda = unir_cadenas('_',[control, periodo])
        
        uri = 'api/recibo/{}/{}'.format(control, periodo)
        ur_full = '{0}/{1}'.format(self.base, uri)

        headers = {'Authorization': 'Token {}'.format(self.token)}

        try:
            response = requests.get(ur_full, headers=headers)
            resp = response.json()

            if response.status_code == 200:
                cadena = unir_cadenas('|', [str(response.status_code), 
                                            datos_busqueda
                                            ])

                log = Log('Log_Buscador_Recibos.txt')
                log.escribir_log('OK', cadena)

                return [response.status_code, resp]
            
            
            else:
                cadena = unir_cadenas('|', [str(response.status_code), 
                                            str(resp),
                                            datos_busqueda
                                            ])
                log = Log('Log_Buscador_Recibos.txt')
                log.escribir_log('ERROR', cadena)


        except:
            cadena = unir_cadenas('|', ['0', 
                                        str(sys.exc_info()[1]),
                                        datos_busqueda
                                        ])
            
            log = Log('Log_Buscador_Recibos.txt')
            log.escribir_log('ERROR', cadena)


            return [ 0, '']



    
