__author__ = 'xianfuxing'
__date__ = '2017/11/17 22:38'

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


# class RegsiterForm2(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': '请输入6-20位非中文字符密码'}))
#     captcha = CaptchaField()
#
#     class Meta:
#         model = UserProfile
#         fields = ('email', 'password')