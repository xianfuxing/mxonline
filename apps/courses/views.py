from django.shortcuts import render
from django.views.generic import View

from .models import Course


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, 'courses/course-list.html', context=context)