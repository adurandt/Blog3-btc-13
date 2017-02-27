from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Publicacion
from .serializers import UserFirstSerializer, UserSecondSerializer, PublicacionFirstSerializer, PublicacionSecondSerializer
from .permissions import GroupPermission

#Vistas basdas en clases

class UserList(APIView):

	def get(self, request):

		user = User.objects.all()
		serializer = UserFirstSerializer(user, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		
		serializer = UserFirtsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		


class UserDetail(APIView):


	#serializer.data es el que nosotros estamos enviando al cliente json

	def get(self, request, pk):

		user = get_object_or_404(User, pk=pk)

		if user is not None:
			serializer = UserFirstSerializer(user)
			return Response(serializer.data, status)

	# modificacion
	def put(seflt, request, pk):
		#traes el objecto de la bd sino envia 404
		user = get_object_or_404(User, pk=pk)

		if user is not None:
			serializer = UserFirstSerializer(instance=user, data=request.data) #compara el objeto
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):

		user = get_object_or_404(User,  pk=pk)


		serializer = UserFirstSerializer(data=request.data)  #data body de http)argumento del serializer, ya que herda de serlializer.ModeSerializer posicional que pasa  através del nombre
		user.delete()
		return Response(status=status.HTTP_2043_NO_CONTENT)


# class de publicacion

#class PublicacionList(APIView):

	#def get(self, request):

		#publicaciones = Publicacion.objects.all()
		#serializer = PublicacionFirstSerializer(publicaciones, many=True)
		#return Response(serializer.data, status=status.HTTP_200_OK)


class PublicacionList(generics.ListCreateAPIView):  # ListCreateAPIView hace el get y post

	queryset = Publicacion.objects.all()
	serializer_class = PublicacionSecondSerializer
	filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend)
	filter_fields = ('fecha',)
	search_fields = ('nombre','contenido','fecha','tags')


	# def get_queryset(self):

	# 	queryset = Publicacion.objects.all()
	# 	name = self.request.query_params.get('publicacion', None)  #query_param  (se inician por ? y se sepoaran &)
	# 	if name is not None:
	# 		queryset = Publicacion.objects.filter(nombre__icontains=name)  #nombre=,  nombre__icontains no case sentive

	# 	return queryset
			

class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Publicacion.objects.all()
	serializer_class = PublicacionSecondSerializer
	#permission_classes = (IsAdminUser,)  # es admin
	#permission_classes = (GroupPermission,)

	