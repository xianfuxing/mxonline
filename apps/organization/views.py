import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import CourseOrg, CityDict
from operation.models import UserFavorite
from .forms import UserAskForm

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Create your views here.


class OrgListView(View):
    def get(self, request):
        # 课程机构
        org_list = CourseOrg.objects.all()
        hot_orgs = org_list.order_by('-click_num')[:3]

        # 城市列表
        cities = CityDict.objects.all()

        # 筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            org_list = org_list.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            org_list = org_list.filter(category=category)

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                org_list = org_list.order_by('-students')
            elif sort == 'courses':
                org_list = org_list.order_by('-course_num')

        org_count = org_list.count()
        page = request.GET.get('page', 1)
        p = Paginator(org_list, 5, request=request)

        try:
            orgs = p.page(page)
        except PageNotAnInteger:
            orgs = p.page(1)

        context = {
            'orgs': orgs,
            'citites': cities,
            'org_count': org_count,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,

        }
        return render(request, 'org/org_list.html', context=context)


class UserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(data=request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save()
            data = {'status': 'success'}
        else:
            error = '填写错误'
            errors = json.loads(user_ask_form.errors.as_json())
            for (kw, error) in errors.items():
                if error[0]['code'] == 'required':
                    error = '表格不完整'
                elif error[0]['code'] == 'invalid_mobile':
                    error = '请正确填写手机号'
                    break
            # m_error = user_ask_form.errors.get('mobile', '')
            # error = '填写错误'
            # if m_error:
            #     error = '请正确填写手机号'
            data = {'status': 'failed', 'msg': error}
        return HttpResponse(json.dumps(data), content_type='application/json')


class OrgHomeView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses = course_org.course_set.all()[:3]
        teachers = course_org.teacher_set.all()

        context = {
            'course_org': course_org,
            'courses': courses,
            'teachers': teachers
        }
        return render(request, 'org/org-detail-homepage.html', context=context)


class OrgCourseView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses = course_org.course_set.all()

        context = {
            'course_org': course_org,
            'courses': courses,
        }
        return render(request, 'org/org-detail-course.html', context=context)


class OrgDescView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))

        context = {
            'course_org': course_org,
        }
        return render(request, 'org/org-detail-desc.html', context=context)


class OrgTeacherView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        teachers = course_org.teacher_set.all()

        context = {
            'course_org': course_org,
            'teachers': teachers,
        }
        return render(request, 'org/org-detail-teachers.html', context=context)


class AddFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            data = {'status': 'fail', 'msg': '用户未登录'}
            return HttpResponse(json.dumps(data), content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 记录存在，表示取消收藏
            exist_records.delete()
            data = {'status': 'success', 'msg': '收藏'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                data = {'status': 'success', 'msg': '已收藏'}
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {'status': 'fail', 'msg': '收藏出错'}
                return HttpResponse(json.dumps(data), content_type='application/json')


