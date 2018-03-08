__author__ = 'xianfuxing'
__date__ = '2017/11/17 22:38'

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext, ugettext_lazy as _
from captcha.fields import CaptchaField
from django.utils.text import capfirst
from django.core.validators import validate_email

from .models import UserProfile
UserModel = get_user_model()


class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        for email in value:
            validate_email(email)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '请输入用户名'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required': '请输入密码'})

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache


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

# class RegsiterForm2(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': '请输入6-20位非中文字符密码'}))
#     captcha = CaptchaField()
#
#     class Meta:
#         model = UserProfile
#         fields = ('email', 'password')