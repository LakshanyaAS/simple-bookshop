"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="home"),
    path('authors/', views.authorpage,name="authors"),
    path('books/',views.bookpage,name="books"),
    path('publishers/',views.publisherpage,name="publishers"),   
    path('addauthor/', views.addauthor, name='addauthor'),
    path('editauthor/<int:id>/', views.editauthor, name='editauthor'),
    path('deleteauthor/<int:id>/', views.deleteauthor, name='deleteauthor'),
    path('addbook/', views.addbook, name='addbook'),
    path('editbook/<int:id>/', views.editbook, name='editbook'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
    path('addpublisher/', views.addpublisher, name='addpublisher'),
    path('editpublisher/<int:id>/', views.editpublisher, name='editpublisher'),
    path('deletepublisher/<int:id>/', views.deletepublisher, name='deletepublisher'),  
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
]





