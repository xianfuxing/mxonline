__author__ = 'xianfuxing'
__date__ = '2017/11/26 23:12'

from django.conf.urls import url
from .views import OrgListView


urlpatterns = [
    url(r'^org-list/$', OrgListView.as_view(), name='org_list')
]