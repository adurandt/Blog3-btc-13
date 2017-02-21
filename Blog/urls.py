"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .api_urls import urlpatterns as api_urls 
from .api_viewset import PublicacionViewset
#from django.conf import settings
#from django.conf.urls.static import static  #para los statics

router = DefaultRouter()  #
router.register(r'^viewsets/$',PublicacionViewset)#url ejemplo viewsets, crea una serie de urls predefinidas (post, get, put ..)
urls = router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('modules.Home.urls')),
    url(r'^home/', include('modules.Home.urls', namespace='Home', app_name='Home')),    
    url(r'^publicaciones/', include('modules.Publicaciones.urls', namespace='Publicaciones', app_name='Publicaciones')),    
    url(r'^api/v1/', include(api_urls)), # url de API
] + urls
#+ static(settings.MEDIA_URL,settings.MEDIA_ROOT) #clase que concatena rutas 2
#+ static(setting.STATIC_URL,settings.STATIC_ROOT)  # clase quedirecciona todo lo que encuentra /static/ a la ruta 