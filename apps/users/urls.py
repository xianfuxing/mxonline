__author__ = 'xianfuxing'
__date__ = '2017/11/17 21:47'

from django.conf.urls import url
from users.views import LoginView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
]