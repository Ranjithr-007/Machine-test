from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import auth, User
from admin1.forms import *
from  user.models import *

# Create your views here.

#Admin Login
def adminlogin(request):
    if request.session.has_key('password'):
        return redirect(adminhome)
    else:
        if request.method=='POST':
            admin_name=request.POST['admin_name']
            password=request.POST['password']
            print(admin_name)
            if admin_name=='admin' and password=='admin':
                request.session['password']=password
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False)

        else:
            return render(request,'Admin/login.html')

#Admin Home
def adminhome(request):
    if request.session.has_key('password'):
        user=User.objects.all()
        employee=Employee.objects.all()
        return render(request,'Admin/home.html',{'user':user,'employee':employee})
    else:
        return redirect(adminlogin)

#User Update
def edit(request,id):
    if request.session.has_key('password'):
        if request.method=='POST':
            name=request.POST['name']
            age=request.POST['age']
            employee = Employee.objects.get(id=id)
            employee.name = name
            employee.age = age
            employee.save()
            return redirect(adminhome)
        else:
            employee=Employee.objects.get(id=id)
            return render(request,'Admin/edit.html',{'employee':employee})
    else:
        return redirect(adminlogin)

#User Delete 
def delete(request,id):
    if request.session.has_key('password'):
        employee=Employee.objects.get(id=id)
        employee.delete()
        return redirect(adminhome)
    else:
        return redirect(adminlogin)

#Admin Logout
def logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(adminlogin)

#Admin Add User
def adduser(request):
    if request.session.has_key('password'):
        if request.method=='POST':
            name=request.POST['name']
            age=request.POST['age']
            department=request.POST['department']
            if Employee.objects.filter(name=name).exists():
                return JsonResponse('user',safe=False)
            else:
                employee = Employee.objects.create(name=name,age=age,department=department)
                employee.save()
                return JsonResponse('true',safe=False)
        else:
            return render(request,'Admin/adduser.html')
    else:
        return redirect(adminlogin)
