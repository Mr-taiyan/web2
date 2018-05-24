from django.shortcuts import render,redirect,render_to_response
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
        context = {'message':'fail'}
        return render(request,'sign_up.html',context)

    user = User_info()
    user.email = email
    user.name = name
    user.pwd = pwd

    user.save()

    context = {'message':'success'}
    return render(request,"sign_in.html",context)
