"""readz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from books import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   path('books/', include('books.urls')),
   path('admin/', admin.site.urls),
   path('home/', views.home, name = 'home'),
   path('login/', views.usr_login, name = 'login'),
   path('register/', views.register, name = 'register'),
   path('post_page/', views.post_page, name = 'post_page'),
   path('post_page1/', views.post_page1, name = 'post_page1'),
   path('profile/', views.profile_page, name = 'profile_page'),
   path('logout/', views.user_logout, name = 'user_logout'),
   path('about/', views.about, name = 'about'),
   path('horror/', views.horror, name = 'horror'),
   path('index/', views.index, name = 'index'),
   
]
