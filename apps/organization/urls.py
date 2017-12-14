__author__ = 'xianfuxing'
__date__ = '2017/11/29 22:15'

from django.conf.urls import url
from .views import OrgListView, UserAskView, OrgHomeView, OrgCourseView


app_name = 'org'
urlpatterns = [
    url(r'^org-list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add-ask/$', UserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='course'),
]