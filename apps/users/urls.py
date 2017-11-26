__author__ = 'xianfuxing'
__date__ = '2017/11/17 21:47'

from django.conf.urls import url
from django.contrib.auth.views import logout
from users.views import LoginView, RegisterView, ActivateUserView, ForgetPwdView, ResetView, ResetPwdView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # url(r'^login/$', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', logout, {'next_page': '/users/login/'}, name='logout'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/activate/(?P<activate_code>.*)/$', ActivateUserView.as_view() ,name='activate'),
    url(r'^forget/$', ForgetPwdView.as_view() ,name='forget'),
    url(r'^reset/(?P<activate_code>.*)/$', ResetView.as_view() ,name='reset'),
    url(r'^reset-password/$', ResetPwdView.as_view() ,name='resetpwd'),
]