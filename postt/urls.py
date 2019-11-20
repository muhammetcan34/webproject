from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [

    url(r'^index/$', views.post_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', views.post_detail, name='detail'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),
]
