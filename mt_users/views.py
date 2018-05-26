from django.shortcuts import render,redirect,render_to_response
from django.http import JsonResponse
from models import *
from django.core.mail import send_mail

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

    if(email == ''):
        context = {'message':'fail'}
        return render(request,'sign_up.html',context)

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

def sign_up_exist(request):
    email = request.GET.get('email')
    count = User_info.objects.filter(email=email).count()
    return JsonResponse({'count':count})


def handle_sign_in(request):
    post = request.POST
    email = post.get('email')
    pwd = post.get('pwd')

    user = User_info.objects.filter(email=email)

    error = render(request,'sign_in.html',context={'check':'1','email':email})
    if(len(user) != 1):
        return error
    elif(pwd != user[0].pwd):
        return error
    else:
        request.session['id'] = user[0].id
        return redirect('/user/')


def user(request):
    user = User_info.objects.get(id=request.session['id'])
    name = user.name
    paid = user.paid
    return render(request,'user.html',context={'name':name,'paid':paid})

def log_out(request):
    del request.session['id']
    return redirect('/')


def ceshi(request):
    id = request.session['id']
    user = User_info.objects.get(id=id)
    user.paid = True
    email = user.email
    # email = 'dennyxineng@gmail.com'

    user.save()

    send_mail('success', 'successful', 'cty9388@163.com',
              [email], fail_silently=False)

    return redirect('/user/')