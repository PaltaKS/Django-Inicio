from django.http import HttpResponse
from django.template import Template, Context
# Request: Para realizar peticiones
# HttpsResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista:
def bienvenida(request): #Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")

def bienvenidaRojo(request): #Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. =)</p>")

    
def miPrimeraPlantilla(request):
    # Abrimos el documento que contiene la plantilla
    plantillaExterna = open(r"C:\Users\SoultKS\Desktop\Django\Proyecto\Proyecto\plantillas\index.html")
    
    # Cargar el documento en una variable tipo Template
    template = Template(plantillaExterna.read())
    
    # Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    
    # Crear un contexto vacío
    contexto = Context()
    
    # Renderizar el documento
    documento = template.render(contexto)
    
    return HttpResponse(documento)