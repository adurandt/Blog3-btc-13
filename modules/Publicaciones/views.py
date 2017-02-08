from django.shortcuts import render


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
	

	return render(request, 'Publicaciones/index.html', {"publicaciones":public})  # (3) contexto en diccionari, para pasar más de una variable