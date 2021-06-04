

import sys
from os import getcwd

import requests
from cryptography.fernet import Fernet

from modulos.txt import ArchivoTxt

class ArchivoTemp():
    def __init__(self):
        self.path    = (getcwd())
        self.archivo = self.path +'\\' +  'data.txt'
        self.key     = Fernet.generate_key()
        self.f       = Fernet(self.key)


    def save_data_user(self, control, password):
        """guarda en archivo temporal el control y password
            del usuario logueado"""

        data  = control  + '|' + password
        token = self.f.encrypt(data.encode())
        archivo = open(self.archivo, 'w')
        archivo.write(token.decode())

    def get_data_user(self):
        """Retorna lista con control y password"""
        try:
            archivo = open(self.archivo, 'r')
            data = archivo.read()
            data_decry = self.f.decrypt(data.encode()).decode()
            data = data_decry.split('|')
            return data
        
        except:
            return []


    def close_temp(self):
        self.temp.close()


class User():
    def __init__(self):
        self.base     = 'http://10.1.2.209:8000'
    def get_database_user(self, control, password):
        """Retorna una lista si es estaff o no el usuario logueado"""
        token_user = Token(control, password)
        token= token_user.get_token_user()
        
        if token[0] == 200:

            uri = 'api/usuario/{}'.format(control)
            ur_full = '{0}/{1}'.format(self.base, uri)
            headers = {'Authorization': 'Token {}'.format(token[1])}
            response = requests.get(ur_full, headers=headers)
            
            if response.status_code == 200:
                return [response.status_code, response.json()[0]]
            else:
                return [response.status_code, response.content]


        else:
            return token

    

class Token:
    def __init__(self, control, password):
        self.control  = control
        self.password = password
        self.base     = 'http://10.1.2.209:8000'


    def get_token_user(self):
        """Retorna el Token del usuario dado"""
        uri = 'api-token-auth/'
        ur_full = '{0}/{1}'.format(self.base, uri)
        params = {
            "username":self.control,
            "password":self.password}
        
        try:
            response = requests.post(ur_full, data = params)

            resp = response.json()
            if response.status_code == 200:
                response_token = resp['token']
                return [response.status_code,response_token]
            else:
                return [response.status_code, resp]
        

        except:
            return [ 0, str(sys.exc_info()[1])]




