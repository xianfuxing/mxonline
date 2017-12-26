from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()

        page = request.GET.get('page', 1)
        p = Paginator(courses, 3, request=request)

        try:
            courses = p.page(page)
        except PageNotAnInteger:
            courses = p.page(1)


        context = {
            'courses': courses
        }
        return render(request, 'courses/course-list.html', context=context)