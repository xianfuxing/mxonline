__author__ = 'xianfuxing'
__date__ = '2017/11/17 21:47'

from django.conf.urls import url
from users.views import user_login


urlpatterns = [
    url(r'^login/$', user_login, name='login'),
]