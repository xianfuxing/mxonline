from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.views.generic import View

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm

from utils.email_send import send_register_email
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')
            if UserProfile.objects.filter(email=username):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '该用户已存在'})
            user_profile = UserProfile()
            # user_profile = register_form2.save()
            user_profile.username = username
            user_profile.email = username
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()

            send_register_email(username, 'register')

            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActivateUserView(View):
    def get(self, request, activate_code):
        msg = '激活失败'
        record = EmailVerifyRecord.objects.get(code=activate_code)
        if record:
            if record.confirmed:
                return render(request, 'login.html', {'msg': '该用户已激活，请登录。'})
            email = record.email
            record.confirmed = True
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
            record.save()

            msg = '激活成功'
        return render(request, 'login.html', {'msg': msg})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            cd = forget_form.cleaned_data
            email = cd.get('email')
            send_register_email(email, 'forget')
            context = {
                'msg': '邮件已发送'
            }

            return render(request, 'login.html', context=context)
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})