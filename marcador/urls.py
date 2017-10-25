from django.conf.urls import url
from .views import bookmark_list, bookmark_user

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', bookmark_user,
        name='marcador_bookmark_user'),
    url(r'^$', bookmark_list, name='marcador_bookmark_list'),
]
