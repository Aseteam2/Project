
from django.shortcuts import render,redirect
from books.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from . import forms
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def home(request):
    dict1={}
    return render(request,"homepage.html",context=dict1)

def post_page(request):
    dict1={}
    return render(request,"postPage.html",context=dict1)    

def usr_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                args={'user':request.user}
                return render(request,'postPage.html',args)
            else:
                return HttpResponse("Account is not active")

        else:
            print("someone else tried login")
            print("username :{} and password {}".format(username,password))
            return HttpResponse("Invalid Details Provided")

    else:
        return render(request, 'login.html',{})                    

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        if user_form.is_valid() :
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            return render(request, 'login.html')
            
        else:
            print(user_form.errors)   
    else: 
        user_form=UserForm()        
    return render(request,"register.html",{'user_form':user_form,registered:'registered'})
