__author__ = 'xianfuxing'
__date__ = '2017/11/17 22:38'

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '请输入用户名'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required': '请输入密码'})


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': '请输入邮箱地址'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required': '请输入密码'})
    captcha = CaptchaField(error_messages={'required': '请输入验证码'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': '请输入邮箱地址'})
    captcha = CaptchaField(error_messages={'required': '请输入验证码'})


class ResetPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, error_messages={'required': '请输入密码'})
    password2 = forms.CharField(required=True, min_length=5, error_messages={'required': '请输入确认密码'})
    captcha = CaptchaField(error_messages={'required': '请输入验证码'})

# class RegsiterForm2(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': '请输入6-20位非中文字符密码'}))
#     captcha = CaptchaField()
#
#     class Meta:
#         model = UserProfile
#         fields = ('email', 'password')