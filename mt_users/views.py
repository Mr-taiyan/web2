from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request,'index.html')

def speaker(request):
    return render(request,'speaker.html')

def introduction(request):
    return render(request,'introduction.html')

def sign_in(request):
    return render(request,'sign_in.html')