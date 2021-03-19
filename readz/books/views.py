
from django.shortcuts import render,redirect
from books.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from . import forms
from datetime import datetime
from django.http import HttpResponse
from .forms import postform
from django.views.generic import CreateView
from books.models import posts
from .models import user_collection
from .forms import bookInputForm
from django.http import FileResponse, Http404

 

# Create your views here.
def home(request):
    dict1={}
    return render(request,"homepage.html",context=dict1)

def exchange(request):
    dict1={}
    return render(request,"bookExchange.html",context=dict1)

def index(request):
    dict1={}
    return render(request,"index.html",context=dict1)    


   
def post_page1(request):
    form = postform()
    if request.session.has_key('username'):
       form.initial['Name']=request.session['username']
    else:
      print("not available")
    if request.method == "POST":
        form = postform(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
        else:
            form = postform()
    return render(request, 'postPage.html', {'form': form}) 


def about(request):
    dict1={}
    return render(request,"AboutUs.html",context=dict1)    


def post_page(request):
    pos = posts.objects.all()
    return render(request,"postPage.html",{'pos':pos})    

def profile_page(request):
    dict1={}
    return render(request,"Profile.html",context=dict1)    

def horror(request):
    dict1={}
    return render(request,"HorrorbookList.html",context=dict1)    

def mystery(request):
    dict1 = {}
    return render(request, "MysterybookList.html", context=dict1)

def travel(request):
    dict1 = {}
    return render(request, "TravelbookList.html", context=dict1)

def romance(request):
    dict1 = {}
    return render(request, "romancebookList.html", context=dict1)

def ebook(request):
    try:
        return FileResponse(open('C:/Users/anmoldeep/Desktop/Project_new/readz/template/ebook.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')

def user_logout(request):
    dict1={}
    return render(request,"homepage.html",context=dict1)   
    
def usr_login(request):
    pos = posts.objects.all()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                args={'user':request.user,'pos':pos}
                print("active")
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



def collection(request):
    # obj = user_collection.objects.get(id=0)
    # print(obj.book_name + "hello world")
    #context = { 'object': obj }

    return render(request , 'Collection.html' )

def book_upload_view(request):
    """Process images uploaded by users"""
    userbooks = user_collection.objects.all()
    if request.method == 'POST':
        form = bookInputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'userCollection.html', {'form': form, 'books': userbooks})
    else:
        form = bookInputForm()
    return render(request, 'userCollection.html', {'form': form,  'books': userbooks})