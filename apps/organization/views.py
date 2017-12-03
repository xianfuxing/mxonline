from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict

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