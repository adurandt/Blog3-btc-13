from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Blog API')


urlpatterns = [
    url(r'^users/', include('modules.Publicaciones.urls_api')),		# http://localhost:8081/api/v1/users/
    url(r'^auth/', obtain_jwt_token),								# http://localhost:8081/api/v1/auth/
    url(r'^documentation/', schema_view),							# http://localhost:8081/api/v1/documentation/
    #TODO agregar publicaciones
]