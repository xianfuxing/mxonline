from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict

# Create your views here.

# Create your views here.


class OrgListView(View):
    def get(self, request):
        orgs = CourseOrg.objects.all()
        cities = CityDict.objects.all()
        org_count = orgs.count()
        context = {
            'orgs': orgs,
            'citites': cities,
            'org_count': org_count
        }
        return render(request, 'org/org_list.html', context=context)