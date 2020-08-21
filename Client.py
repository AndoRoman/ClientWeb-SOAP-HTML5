from zeep.client import Client
import zeep
##CLIENT SOAP
settings = zeep.Settings(strict=False, xml_huge_tree=True)
#wsdl = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'
#cliente = Client(wsdl)
#Factory more information on Doc : https://docs.python-zeep.org/en/master/datastructures.html
#factory = cliente.type_factory('http://soap.eict.pucmm.edu/')

def NewForm(nombre, sector, latitud, longitud, foto):
    return True


def authentication(user, password):
    if user == 'admin' and password == 'admin':
        person = True

    return person
