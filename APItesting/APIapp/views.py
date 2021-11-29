from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from .Auth.auth import token_dict,DNAC
import os

DNAC_URL=DNAC.DNAC_URL
DNAC_USER=DNAC.DNAC_USER
DNAC_PASS=DNAC.DNAC_PASS

class EndPoints:
    def index(request):
        return render(request,'index.html',context=token_dict)


    def token(request):
        url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)
        print(url)
        header = {'content-type': 'application/json'}
        response = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=header)
        token = response.json()['Token']
        print("token : {}".format(token))
        token_dict={'token':format(token)}
        return render(request,'token.html',context=token_dict)

    def get_vlan_from_dnac(request):
        token = token_dict['token']
        response = requests.get("https://{}/dna/intent/api/v1/topology/vlan/vlan-names".format(DNAC_URL),
        headers={
                "X-Auth-Token": "{}".format(token),
                "Content-type": "application/json",
            },
            verify=False
        )

        print(response.status_code)
        return HttpResponse(response)

    def get_site_from_dnac(request):
        token=token_dict['token']
        response = requests.get("https://{}/dna/intent/api/v1/site".format(DNAC_URL),
        headers={
                "X-Auth-Token": "{}".format(token),
                "Content-type": "application/json",
            },
            verify=False
        )
        response_dict=response.json()
        print(type(response_dict))
        return render(request,'page.html',context=response_dict)
        #returns to a json format
        #return HttpResponse(response,content_type='application/json')
        # Downloads to a text file
        #return HttpResponse(response,content_type='application/text')


    def get_device_family(request):
        token=token_dict['token']
        response = requests.get("https://{}/dna/intent/api/v1/image/importation/device-family-identifiers".format(DNAC_URL),
        headers={
                "X-Auth-Token": "{}".format(token),
                "Content-type": "application/json",
            },
            verify=False
        )
        print(response.status_code)
        return HttpResponse(response)

    def get_site_health(request):
            token=token_dict['token']
            response = requests.get("https://{}/dna/intent/api/v1/site-health".format(DNAC_URL),
            headers={
                    "X-Auth-Token": "{}".format(token),
                    "Content-type": "application/json",
                },
                verify=False
            )
            assert (response.status_code)==200
            return HttpResponse(response)