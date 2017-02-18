from django.contrib import admin
from .models import Publicacion

# clase por modelo, en esta calse de hace el custom admin.
class PublicacionAdmin(admin.ModelAdmin):
	pass

# mandamos la clase de regiuster que registra los modelos dentro del administrador, se hace por cada modelo uqe agreguemos.	
admin.site.register(Publicacion, PublicacionAdmin)	