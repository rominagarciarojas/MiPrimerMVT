from datetime import datetime
from django.http import HttpResponse


def  saludo(request):
    
    return HttpResponse("Hola alumnos...")



