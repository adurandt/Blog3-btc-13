from django.conf.urls import url, include
from .views import index, contactos, login, singup, Logout


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contactos/$', contactos, name='contactos'),
    url(r'^login/$', login, name= 'login'),
    url(r'^signup/$', singup, name='signup'),
    url(r'^logout/$', Logout, name='logout'),
]	