from zeep.client import Client
import zeep

##CLIENT SOAP
settings = zeep.Settings(strict=False, xml_huge_tree=True)
wsdl = 'http://localhost:8043/ws/FormularioWebServices?wsdl'
cliente = Client(wsdl)
# Factory more information on Doc : https://docs.python-zeep.org/en/master/datastructures.html
factory = cliente.type_factory('http://soap/')


def NewForm(nombre, sector, nivelEscolar, usuario, latitud, longitud, picture):

    ubication = factory.ubicacion(longitud, latitud)
    nuevoForm = factory.formulario(nombre=nombre, sector=sector, nivelEscolar=nivelEscolar, usuario=usuario, ubicacion=ubication, foto=picture)

    if nuevoForm is not None:
        print(nuevoForm)
        return True
    else:
        return False



def authentication(user, password):
    if user == 'admin' and password == 'admin':
        person = True

    return person


def getForms():
    return cliente.service.getFormulario()
