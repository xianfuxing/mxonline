from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')