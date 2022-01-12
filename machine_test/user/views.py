from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from . models import *

# Create your views here.

#User Home
def home(request):
    if request.user.is_authenticated:
        return render(request,'User/home.html')
    else:
        return redirect(user_login)

#User Register
def user_signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            if User.objects.filter(username=username).exists(): 
                return JsonResponse('user', safe=False)
            elif User.objects.filter(email=email).exists():
                return JsonResponse('user', safe=False)
            elif UserData.objects.filter(phone=phone).exists():
                return JsonResponse('phone', safe=False)
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user = UserData.objects.create(phone = phone,user = user)
                return JsonResponse('true', safe=False)
        
        else:
            return render(request, 'User/register.html')

#User Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return render(request, 'User/login.html')

#User Logout

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(user_login)


