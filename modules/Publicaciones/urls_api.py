from django.conf.urls import url
from .api_views  import UserList, UserDetail, PublicacionList, PublicacionDetail

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^(?P<pk>[0-9])+/$', UserDetail.as_view()),
    url(r'^publicaciones/$', PublicacionList.as_view(), name='api-list-publicacion'),
    url(r'^publicaciones/(?P<pk>[0-9])+/$', PublicacionDetail.as_view(), name='api-detail-publicacion'),
]