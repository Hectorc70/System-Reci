import requests

from login.login import User



import sys

class Cliente():


    def __init__(self, token):
        self.token = token
        self.base     = 'http://10.1.2.209:8000'




    def enviar_empleado(self):
        pass

    def enviar_datos_recibo(self):
        uri = 'api/recibo/'
        ur_full = '{0}/{1}'.format(self.base, uri)
        headers = {'Authorization': 'Token {}'.format(self.token)}
        params = {
                "nombre_archivo":"Archivo Prueba",
                "ruta_archivo":"C:\\PRUEBA\\ARCHIVO1",
                "periodo":"202101",
                "tipo_nomina":"ORDINARIA_PRUEBA",
                "no_control":"318212"
                }

        try:
            response = requests.post(ur_full, headers=headers, data = params)
            resp = response.json()

            if response.status_code == 200 or response.status_code == 201:
                response_token = resp['token']
                return [response.status_code,response_token]

            else:
                return [response.status_code, resp]
        
        except:
            return [ 0, str(sys.exc_info()[1])]


