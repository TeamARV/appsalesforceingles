
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http.response import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


from simple_salesforce import Salesforce

def testf1(request):
    # Configura los detalles de conexión con Salesforce
    username = 'riveravegaandres@wise-hawk-b8wjs3.com'
    password = '+pastdostrescuatroX59'
    security_token = '3MVG9g9rbsTkKnAXRU_hOLvHRYnx8qJ_AO2DpfdGUKxIj8wClK1IGCwGRFR0ZMc4qtjH5tgr2EGMdobzpa7_G'
    #sandbox = False  # Establecer en True si estás usando un sandbox de Salesforce

    # Crea una instancia del cliente Salesforce
    sf = Salesforce(username=username, password=password, security_token=security_token)

    # Ahora puedes utilizar los métodos de la instancia "sf" para interactuar con Salesforce,
    # como consultar datos, crear registros, actualizar registros, etc.

    # Ejemplo: Consultar algunos registros de Salesforce
    consulta_resultados = sf.query("SELECT Id, Name, Email FROM Contact LIMIT 5")

    # El resultado se encuentra en consulta_resultados['records']

    # Puedes pasar los resultados a tu template para mostrarlos en tu vista HTML
    context = {
        'resultados': consulta_resultados['records'],
    }

    return render(request, 'testf1.html', context)

