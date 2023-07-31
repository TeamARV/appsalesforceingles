
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http.response import HttpResponse

from simple_salesforce import Salesforce
from requests.auth import HTTPBasicAuth
import requests
import json



# Create your views here.


def index(request):
    return render(request, 'index.html')


def game(request):
    return render(request, 'game.html')



def testf1(request):



    CONSUMER_KEY = '3MVG99gP.VbJma8UueUneeXfQ6jjTlMjJX1Xsp8k7u.eMJX27iWaltPgaM3oJI5sqGdsJcdj8u6ZZMtGCmgYu'
    CONSUMER_SECRET= 'E930064C14C5E307B8AD6229F742C184E15D16CA17EBEA0A134E540DC17E3BB3'
    USERNAME ='riveravegaandres@wise-hawk-b8wjs3.com'
    PASSWORD ='+pastdostrescuatroX939'
    DOMAIN = 'https://login.salesforce.com'
    DOMAIN_NAME = DOMAIN
    DOMAIN_NAME2='https://wise-hawk-b8wjs3-dev-ed.trailblaze.my.salesforce.com'

    json_data = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD,
    'client_id': CONSUMER_KEY,
    'client_secret': CONSUMER_SECRET,
    'content-type': 'application/json'
}


    

    uri_token_request = DOMAIN_NAME + '/services/oauth2/token'
    response = requests.post(uri_token_request, data=json_data)
    print( response.json())
    access_token = response.json()['access_token']
    print('el token access --->' + access_token)

    url = 'https://wise-hawk-b8wjs3-dev-ed.trailblaze.my.salesforce.com/services/data/v52.0/limits'

    headers = {
	'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}
    response1 = requests.get(DOMAIN_NAME2 + '/services/data/v53.0/query/?q=SELECT+Id,CreatedById,Name,WordES__c,WordIN__c+FROM+Diccionario__c limit 10', headers=headers)
    print(response.json())

    response1 = response1.json()

    # Realizar la solicitud GET a la API de límites
    response = requests.get(url, headers=headers)

    # Obtener la respuesta en formato JSON
    limits_data = response.json()

    #Imprimir los límites y el uso actual
    for limit_name, limit_value in limits_data.items():
        print(f'{limit_name}: {limit_value["Max"]} (usado: {limit_value["Remaining"]})')






    return render(request, 'testf1.html', {'response': response1})



