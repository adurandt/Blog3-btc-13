from django.conf.urls import url
from .views  import index, add

urlpatterns = [
    url(r'^$', index, name='index-publicacion'),
    url(r'^add/$', add, name='add-publicacion'),
]