__author__ = 'xianfuxing'
__date__ = '2017/12/14 23:48'


from django import template
from django.core.urlresolvers import reverse


register = template.Library()

@register.simple_tag()
def is_active(request, *url_strings):
    for urlpattern in url_strings:
        if urlpattern in request.path:
            return 'active2'
        return ''
