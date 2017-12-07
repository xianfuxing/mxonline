__author__ = 'xianfuxing'
__date__ = '2017/11/29 22:15'

from django.conf.urls import url
from .views import OrgListView


app_name = 'org'
urlpatterns = [
    url(r'^org-list/$', OrgListView.as_view(), name='org_list')
]