from django.shortcuts import render
from .models import *
from django.db import connection
from datetime import datetime

# Create your views here.
def index(request):
    x=Product.objects.all().order_by('-id')[0:10]
    mdict={"prod":x}
    return render(request,'user/index.html',context=mdict)
#####################################################


def about(request):
    return render(request,'user/about.html')
#####################################################


def contact(request):
    Status=False
    if request.method=="POST":
        a=request.POST.get("name")
        b= request.POST.get("address")
        c= request.POST.get("mob")
        d=request.POST.get("email")
        e=request.POST.get("password")
        register(Name=a,Address=b, Mob=c, Email=d, Password=e).save()
        Status=True
    msg={"m":Status}
    return render(request,'user/contact us.html',context=msg)
#####################################################


def Myorder(request):
    return render(request,'user/MyOrder.html')
#####################################################

def product(request):
    return render(request,'user/product.html')
#####################################################


def signin(request):
    return render(request,'user/sign in.html')
#####################################################

# def index(request):
#     return render(request,'/user/index.html')
#####################################################

def viewproduct(request):
    a=request.GET.get('msg')
    x=Product.objects.all().filter(id=a)
    mdict={"pdata":x}
    return render(request,'user/viewproduct.html',context=mdict)

def mens(request):
    x=maincategory.objects.all()
    y=Product.objects.all().filter()
    mdict={"pdata":x ,"mdata":y}
    return render(request,'user/mens.html',context=mdict)

def womens(request):
    return render(request,'user/womens.html')
def kids(request):
    return render(request, "user/kids.html")