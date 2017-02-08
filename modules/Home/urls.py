from django.conf.urls import url, include
from .views import index, contactos, otros, saludo, suma, compara


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contactos$', contactos, name='contactos'),
    url(r'^otros/(?P<num>[0-9]+)/$', otros, name='otros'),
    url(r'^saludo/(?P<name>[\w\s]+/$)', saludo, name='saludo'),
    url(r'^suma/(?P<x>[0-9]+)/$', suma, name='suma'),
    url(r'^suma/(?P<x>[0-9]+)/(?P<y>[0-9]+)/$', suma, name= 'suma'),
    url(r'^compara/(?P<x>[0-9]+)/(?P<y>[0-9]+)/$', compara, name='compara')
]	