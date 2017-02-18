#functions.py
''' fuciones que no dependen de la logica y se ocupan más de una vez
'''

import os
from django.conf import settings

def hadle_upload_file(f, name):
	root = settings.MEDIA_ROOT  + '/Publicaciones' + name 
	with open(root, 'wb+') as destination:
		for chunk in f.chunks():  #arreglo de pedazos binarios
			destination.write(chunk)

	return root		

