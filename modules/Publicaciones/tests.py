from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Publicacion
from django.contrib.auth.models import User
import json

class PublicacionTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_superuser(username="test", password="us3rT3st", email="test@gmail.com")
		#user = User.objects.get(id=2)
		self.data = {"nombre":"Otra Publicacion", "contenido":"aasasasasassa","tags":"TC", "autor":self.user.id}
		self.url = reverse('api-list-publicacion')
		print(self.url)

	# test_	
	def test_list_publicaciones(self):
		
		response = self.client.get(self.url) #client viene implicito en la clase APITestCase
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	
	def test_create_publicacion(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		#self.assertEqual(response.data, self.data) #falla

class PublicacionDetailTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_superuser(username="test", password="us3rT3st", email="test@gmail.com")
		self.publicacion = Publicacion(nombre="Otra Publicacion", contenido="aasasasasassa", tags="TC", autor=self.user)
		self.publicacion.save()
		self.url = reverse("api-detail-publicacion", args=[self.publicacion.id])

	def test_retrive_publicacion(self):
		
		response = self.client.get(self.url)
		print(response.content)
		self.assertEqual(response.status_code, status.HTTP_200_OK)	

	def test_update_publicacion(self):
		self.data = {"nombre":"Otra Publicacion","contenido":"aasasasasassa","fecha":"2017-02-21","tags":"TC","autor":2}
		response = self.client.put(self.url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, self.data)

	def test_delete_publicacion(self):
		response = self.client.delete(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_403_OK)	
, 



		