
from django.shortcuts import render,redirect,get_object_or_404
from books.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.conf import settings
from . import forms
from datetime import datetime
from django.http import HttpResponse
from .forms import postform
from django.views.generic import CreateView
from books.models import posts
from books.models import user_collection
from books.forms import bookInputForm
from .forms import commentform
from django.http import FileResponse, Http404, HttpResponseRedirect
from .models import book_exchange
from .models import Comment
from .models import horror
from .models import romantic
from .models import mystery
from .models import travel
from readz.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView


# Create your views here.
# Views are the function which perform an action for specific url. For instance, it defines which html page is to be opened after
# entering url and what action is to be performed on the form or anything else included in that page.
def home(request):
    dict1={}
    return render(request,"homepage.html",context=dict1)

def exchange(request):
    dict1={}
    if request.method == "POST":
        print(request.POST)
        request_type_in = request.POST.get('request_type')
        requester_name_in = request.POST.get('requester_name')
        book_name_in = request.POST.get('book_name')
        email_in = request.POST.get('email')
        phone_in = request.POST.get('phone')
        address_in = request.POST.get('address')
        # saving data to model
        book_exchange.objects.create(request_type = request_type_in, requester_name= requester_name_in, book_name=book_name_in, email = email_in, phone=phone_in, address=address_in)

        #sending conformation email
        subject = "Request Conformation"
        message = "Your request for book exchange named "+ book_name_in + " has been received and will soon be processed"
        recepient = email_in
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request,"bookExchange.html",{'request': 'Successful'})
    return render(request,"bookExchange.html", {'request': ''})

def index(request):
    dict1={}
    return render(request,"index.html",context=dict1)    


   
def post_page1(request):
    pos = posts.objects.all()
    form = postform()
    args={'form': form,'pos':pos}
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
    return render(request, 'postPage.html', args) 

def about(request):
    dict1={}
    return render(request,"AboutUs.html",context=dict1)    

def post_page(request):
    pos = posts.objects.all()
    return render(request,"postPage.html",{'pos':pos})    

def profile_page(request):
    dict1={}
    return render(request,"Profile.html",context=dict1)    

def horror1(request):
    hor = horror.objects.all()
    return render(request,"HorrorbookList.html", {'hor': hor})    

def mystery1(request):
    mys = mystery.objects.all()
    return render(request, "MysterybookList.html",{'mys': mys })

def travel1(request):
    tr = travel.objects.all()
    return render(request, "TravelbookList.html", {'tr':tr})

def romance1(request):
    ro = romantic.objects.all()
    return render(request, "romancebookList.html", {'ro':ro})

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




def LikeView(request,pk):
    post = get_object_or_404(posts,id=request.POST.get('post_id'))
    post.likes.add(request,user)
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class AddCommentView(CreateView):
    model=Comment
    form_class = commentform
    template_name= 'comments.html'

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

    
    