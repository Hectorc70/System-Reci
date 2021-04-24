import requests

class User:
    def __init__(self, control, password):
        self.control  = control
        self.password = password
        self.base     = 'http://127.0.0.1:8000'


    def __get_token_user(self):
        """Retorna el Token del usuario dado"""
        uri = 'api-token-auth/'
        ur_full = '{0}/{1}'.format(self.base, uri)
        params = {"username":self.control,
                "password":self.password}

        response = requests.post(ur_full, data = params)

        resp = response.json()
        if response.status_code == 200:
            response_token = resp['token']
            return [response.status_code,response_token]
        else:
            return [response.status_code, resp]


    def login(self):
        token= self.__get_token_user()
        
        if token[0] == 200:

            uri = 'api/usuario/{}'.format(self.control,)
            ur_full = '{0}/{1}'.format(self.base, uri)
            headers = {'Authorization': 'Token {}'.format(token[1])}
            response = requests.get(ur_full, headers=headers)
            
            if response.status_code == 200:
                return [response.status_code, response.json()[0]]
            else:
                return [response.status_code, response.content]


        else:
            return token
