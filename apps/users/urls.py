__author__ = 'xianfuxing'
__date__ = '2017/11/17 21:47'

from django.conf.urls import url
from users.views import LoginView, RegisterView, ActivateUserView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/activate/(?P<activate_code>.*)/$', ActivateUserView.as_view() ,name='activate'),
]