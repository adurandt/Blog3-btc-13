from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login as log, logout


def index(request):
	user = request.user

	return render(request, 'Home/index.html',{"user":user})

def contactos(request):

	return HttpResponse('<b>Pagina de Contactos</b>')

def singup(request):
		if request.method == 'POST':
			firts_name = request.POST['firts_name']
			last_name = request.POST['last_name']
			username = request.POST['username']
			password = request.POST['password']

			user = User.objects.get(username=username)
			if user is None:

				user = User.objects.create_user(
					first_name = first_name,
					last_name = last_name,
					username = username,
					password = password
				)
				user.save()

				return HttpResponse('<b>Usuario Registrado</b>')

			else:

				return HttpResponse('<b>Usuario ya Existe</b>')	
			
		else:

			return render(request, "Home/signup.html")		

def login(request):
		
		if request.method == 'POST':
			
			user = authenticate(username=request.POST['username'],
			password=request.POST['password'])

			if user is not None:
				log(request, user)
				return redirect('Home:index')

			else:

				return HttpResponse("Error en usuario o contraseña")

		else:

			return render(request, 'Home/login.html')

def Logout(request):
	logout(request)
	return redirect('Home:index')

