__author__ = 'xianfuxing'
__date__ = '2017/11/26 23:12'

from django.conf.urls import url
from .views import CourseListView


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list')
]