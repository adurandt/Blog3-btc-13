from rest_framework import serializers
from .models import Publicacion
from django.contrib.auth.models import User

#class UserSerializer(serializers.Serializer):

	#nombre = serializer.CharField() # first_name
	#apellidos = serializer.CharField()
	#email = serializer.EmailField()
	#is_active = serializer.BooleanField()

class PublicacionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Publicacion
		fields = ("nombre", "contenido", "fecha", "tags")


class UserFirstSerializer(serializers.ModelSerializer):

	publicaciones = PublicacionSerializer(read_only=True, many=True)  # many muchos los oabjetos que pueden venir relacionados

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email', 'publicaciones')
		#fields = ('__ALL__')


class UserSecondSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		exclude = ('is_active	',)


class PublicacionFirstSerializer(serializers.ModelSerializer, serializers.Serializer):

	autor_nombre = serializers.CharField(source='autor.first_name')
	autor_apellidos = serializers.CharField(source='autor.last_name')


	class Meta:
		model= Publicacion
		fields = ("nombre", "contenido", "fecha", "tags", "autor", "autor_nombre", "autor_apellidos")

class PublicacionSecondSerializer(serializers.ModelSerializer, serializers.Serializer):

	class Meta:
		model= Publicacion
		fields = ("nombre", "contenido", "fecha", "tags", "autor")
		