__author__ = 'xianfuxing'
__date__ = '2017/11/26 23:12'

from django.conf.urls import url
from .views import CourseListView, CourseDeailView, CourseLessionView


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDeailView.as_view(), name='course_detail'),
    url(r'^lession/(?P<course_id>\d+)/$', CourseLessionView.as_view(), name='course_lession'),
]