from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        sort =  request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                courses = courses.order_by('-click_nums')
            elif sort == 'students':
                courses = courses.order_by('-students')
        else:
            courses = courses.order_by('-add_time')

        page = request.GET.get('page', 1)
        p = Paginator(courses, 3, request=request)

        try:
            courses = p.page(page)
        except PageNotAnInteger:
            courses = p.page(1)

        context = {
            'courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
        }
        return render(request, 'courses/course-list.html', context=context)


class CourseDeailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)

        tag = course.tag
        if tag:
            related_course = Course.objects.filter(tag=tag)[:1]
        else:
            related_course = []

        context = {
            'course': course,
            'related_course': related_course
        }
        return render(request, 'courses/course-detail.html', context=context)


class CourseLessionView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)

        context = {
            'course': course
        }

        return render(request, 'courses/course-video.html', context=context)