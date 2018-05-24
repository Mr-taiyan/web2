from django.shortcuts import render,redirect
from models import *

# Create your views here.

def welcome(request):
    return render(request,'index.html')

def speaker(request):
    return render(request,'speaker.html')

def introduction(request):
    return render(request,'introduction.html')

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')

def handle_sign_up(request):
    post = request.POST
    email = post.get("email")
    pwd = post.get("pwd")
    cpwd = post.get("cpwd")
    name = post.get("name")

    if(pwd != cpwd):
        return redirect('/sign_up/')

    user = User_info()
    user.email = email
    user.name = name
    user.pwd = pwd

    user.save()

    return redirect("/sign_in/")
