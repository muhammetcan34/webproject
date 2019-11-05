from django.conf.urls import url

from home.views import home_view
from.views import *

app_name = 'post'


urlpatterns = [


    url(r'^index/$', post_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', post_detail, name='detail'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete'),
]