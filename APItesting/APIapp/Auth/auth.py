import requests
from requests.auth import HTTPBasicAuth
import os
#from decouple import config

os.environ['DNAC_URL']="sandboxdnac.cisco.com"
os.environ['DNAC_USER']="devnetuser"
os.environ['DNAC_PASS']="Cisco123!"

DNAC_URL = os.environ.get('DNAC_URL')
DNAC_USER = os.environ.get('DNAC_USER')
DNAC_PASS = os.environ.get('DNAC_PASS')

class Auth:
    def token_generation():
        url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)
        header = {'content-type': 'application/json'}
        response = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=header)
        token = response.json()['Token']
        print("Token : {}".format(token))
        token_dict={'token':format(token)}
        return token_dict

token_dict = Auth.token_generation()
