import requests

class User:
    def __init__(self, control, password):
        self.control  = control
        self.password = password
        self.base     = 'http://127.0.0.1:8000'


    def get_token_user(self):
        uri = 'api-token-auth/'
        ur_full = '{0}/{1}'.format(self.base, uri)
        params = {"username":self.control,
                "password":self.password}

        response = requests.post(ur_full, data = params)
        response.content
        
        if response.status_code == 200:
            response_token = response.json()['token']
            return [response.status_code,response_token]
        else:
            return [response.status_code, response.content]