__author__ = 'xianfuxing'
__date__ = '2017/11/17 21:47'

from django.conf.urls import url
from django.contrib.auth.views import logout
from users.views import LoginView, RegisterView, ActivateUserView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', logout, {'next_page': '/users/login/'}, name='logout'),
    url(r'^logout/$', LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/activate/(?P<activate_code>.*)/$', ActivateUserView.as_view() ,name='activate'),
]