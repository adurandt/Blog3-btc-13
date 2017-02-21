#api_viewset.py

from rest_framework import viewsets
from .models import Publicacion
from .serializers import PublicacionSecondSerializer

class PublicacionViewset(viewsets.ViewSet):

	queryset = Publicacion.objects.all()
	serializer_class = PublicacionSecondSerializer
