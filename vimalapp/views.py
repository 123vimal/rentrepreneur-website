from datetime import date, datetime
from importlib.resources import path
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from visions import EmailAddress
from vimalapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#for login user vimal123 and pass. is %4098vimal    

# Create your views here.
def home(request):
    return render(request, "index.html")

def career(request):
    return render(request,"career.html")
    

def Start_Buisness_with_Me(request):
    return render(request, "start_buisness_with_me.html")

def contact(request):
    if request.method == "POST":
        Firstname= request.POST.get('Firstname')
        Lastname= request.POST.get('Lastname')
        Phone= request.POST.get('Phone')
        Username= request.POST.get('Username')
        City = request.POST.get('City')
        State= request.POST.get('State')
        contact=Contact(Firstname=Firstname, Lastname=Lastname, Phone=Phone, Username=Username, State=State, 
        City=City, date=date.today())
        contact.save()
        messages.success(request, 'Your massage has been sent!')

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def loginuser(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        #Check if user has entered correct credentials
        user = authenticate(request, username='username', password='password')
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/home')
        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")

def logout(request):
    logout(request)
    return redirect('/login')

# def signup(request):
#     return render(request, "singup.html")