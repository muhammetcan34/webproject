from django.conf.urls import url
from.views import *

app_name = 'home'


urlpatterns = [


    url(r'^home/$', home_view, name='home'),

]