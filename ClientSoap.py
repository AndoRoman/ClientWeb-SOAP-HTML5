from zeep.client import Client
import zeep

# CLIENT SOAP
settings = zeep.Settings(strict=False, xml_huge_tree=True)
wsdl = 'http://localhost:8043/ws/FormularioWebServices?wsdl'

cliente = Client(wsdl)
# Factory more information on Doc : https://docs.python-zeep.org/en/master/datastructures.html
factory = cliente.type_factory('http://soap.clienteHTML5/')


# List forms
def getForms(user):
    return cliente.service.getFormularioPorUsuario(user)


# Create New Forms
def NewForm(nombre, sector, nivelEscolar, usuario, latitud, longitud, picture):
    forms = cliente.service.getFormulario()
    id_global = len(forms)
    nuevoForm = factory.formularioIndexDB(nombre=nombre, sector=sector, nivelEscolar=nivelEscolar,
                                          latitud=latitud, longitud=longitud, id=id_global,
                                          usuario=usuario, foto=picture)
    id_global += 1
    print(nuevoForm)
    return cliente.service.agregarRegistro(nuevoForm)


# Authenticar User
def authentication(user, password):
   return cliente.service.autenticarUsuario(user, password)
