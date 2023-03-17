from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path("",views.home,name="home"),
   path("home",views.home,name="home"),
   path("start_buisness_with_me",views.Start_Buisness_with_Me,name="Start_Buisness_with_Me"),
   path("about",views.about,name="about"),
   path("contact",views.contact,name="contact"),
   path("career",views.career,name="career"),
   path("services",views.services,name="services"),
   path("login",views.loginuser,name="login")
   
] 
