from django.shortcuts import render, redirect
from  .models import TAGS, Publicacion
from .functions import hadle_upload_file


def index(request):

	public = [
		{	"nombre":"Mi primer Proyecto en Django",
			"autor":"Alberto Durand",
			"fecha":"07-02-2017",
			"raiting":5
		},

		{	"nombre":"Mi segundo Proyecto en Django",
			"autor":"Jose Carlos Sandoval",
			"fecha":"01-02-2017",
			"raiting":3
		},

		{	"nombre":"Mi tercer Proyecto en Django",
			"autor":"Javier Fernandez",
			"fecha":"01-01-2017",
			"raiting":2
		}
	]
	

	return render(request, 'Publicaciones/index.html', {"publicaciones":public})  # (2) Template html, (3) contexto en diccionari, para pasar más de una variable

def add(request):

	if request.method == 'POST':
		types = {'image/jpeg':'.jpg', 'image/png':'.png', 'image/gif': '.gif'}  #simula un switch en python
		image_name = request.FILES['imagen'].name + types[request.FILES['imagen'].content_type]
		if request.user.is_authenticated():
			publicacion = Publicacion()
			publicacion.nombre = request.POST['nombre']
			publicacion.contenido = request.POST['contenido']	
			publicacion.tags = request.POST['tag']
			publicacion.autor = request.user
			publicacion.imagen = hadle_upload_file(request.FILES['imagen'], image_name) # iamge_name = nombre del archivo

			publicacion.save()

			return redirect('Publicaciones:index-publicacion')


	else:
		dict_tags = dict((x,y) for x,y in TAGS)
		return render(request, 'Publicaciones/add.html', { "tags":dict_tags})	
