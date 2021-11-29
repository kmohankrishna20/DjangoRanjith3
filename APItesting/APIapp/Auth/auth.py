import requests
from requests.auth import HTTPBasicAuth
import os
from .conf import DNAC
class Auth:
    def __init__(self,DNAC):
        self.DNAC_URL=DNAC.DNAC_URL
        self.DNAC_USER=DNAC.DNAC_USER
        self.DNAC_PASS=DNAC.DNAC_PASS

    def token_generation(self):
        self.url = 'https://{}/dna/system/api/v1/auth/token'.format(self.DNAC_URL)
        print(self.url)
        self.header = {'content-type': 'application/json'}
        response = requests.post(self.url, auth=HTTPBasicAuth(self.DNAC_USER, self.DNAC_PASS), headers=self.header)
        self.token = response.json()['Token']
        print("Token : {}".format(self.token))
        token_dict={'token':format(self.token)}
        return token_dict

token_dict= Auth(DNAC).token_generation()
