__author__ = 'xianfuxing'
__date__ = '2017/11/29 22:15'

from django.conf.urls import url
from .views import OrgListView, UserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView,\
    AddFavView


app_name = 'org'
urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add-ask/$', UserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='desc'),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='teacher'),
    url(r'^add-fav/$', AddFavView.as_view(), name='add_fav'),
]