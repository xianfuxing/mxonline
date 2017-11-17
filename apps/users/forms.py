__author__ = 'xianfuxing'
__date__ = '2017/11/17 22:38'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)