from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'Home/index.html')

def contactos(request):
	return HttpResponse('<b>Pagina de Contactos</b>')

def otros(request, num):
	return HttpResponse('Página de otros número: <b>' + num + '</b>')

def saludo(request, name):
	return HttpResponse('Hola, <b><i>{}</i></b> bienvenido!!!'.format(name))

def suma(request, x, y):
	suma = int(x) + int(y)
	return HttpResponse('La suma de <i>{}</i> más <i>{}</i> es: <b>{}</b>'.format(x,y,suma))

def compara(request, x, y):
	if int(x) > int(y):
		compara = (x,y)
	else:
		compara = (y,x)
	return HttpResponse('El valor de %s es mayor que %s' % compara)