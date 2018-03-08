__author__ = 'xianfuxing'
__date__ = '2017/12/14 23:48'


from django import template
from django.core.urlresolvers import reverse

from operation.models import UserFavorite


register = template.Library()


@register.simple_tag()
def is_active(request, *url_strings):
    for urlpattern in url_strings:
        if urlpattern in request.path:
            return 'active2'
        return ''


@register.simple_tag()
def is_active_reverse(request, args, *urlnames):
    for urlname in urlnames:
        if args:
            args = [args]
        else:
            args =[]
        url = reverse(urlname, args=args)
        if url in request.path:
            if url == '/' and request.path == '/':
                return 'active2 active'
            elif url == '/' and request.path != '/':
                return ''
            return 'active2 active'
        return ''


@register.simple_tag()
def is_fav(request, id, fav_type):
    if request.user.is_authenticated():
        fav = UserFavorite.objects.filter(user=request.user, fav_id=id, fav_type=fav_type)
    else:
        fav = None
    if fav:
        return '已收藏'
    else:
        return '收藏'