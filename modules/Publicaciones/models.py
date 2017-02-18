from django.db import models
from django.contrib.auth.models import User # modelo generico de django

TAGS = (
	('TC', 'Tecnología'),
	('CT', 'Científico'),
	('PR', 'Programación')
)

# Manager
#class carlossgPublicacionesManager(models.Manager):

	#def get_queryset(self):
	#	return super(carlossgPublicacionesManager,self).get_queryset().filter(autor__usermame='carlossg')

class Publicacion (models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	contenido = models.TextField()
	fecha = models.DateField(auto_now_add=True)
	autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publicaciones")  #related_name es el nombre de la relacion
	tags = models.CharField(choices=TAGS, max_length=50) # opciones de eleccción
	imagen = models.ImageField(upload_to='Publicaciones/', null=True, blank=True) # para el admin, null puede o no haber vacio, blank pone todos blancos

	# Manager
	#carlossg_publicacion = carlossgPublicacionesManager()

	#da nombre al objeto	
	def __str__(self):
		return "%s %s" % ("Publicacion: " , self.nombre)


