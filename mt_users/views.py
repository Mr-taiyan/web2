from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request,'index.html')

def ceshi(request):
    return render(request,'ceshi.html')
