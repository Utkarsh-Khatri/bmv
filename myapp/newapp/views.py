from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import hall

# Create your views here.
def home(request):
    return render(request,"home.html")
def SaveEnquiry(request):
    if request.method=='POST':
        uname=request.POST.get('cust_name')
        email=request.POST.get('cust_email')
        password=request.POST.get('password')
        phone=request.POST.get('phn_no')
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken. Please choose a different username.", status=400)
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return HttpResponse("User has been registered successfully")
        print(uname,email,password,phone)
    return render(request, "SignUp.html")
def homea(request):
    products = hall.objects.all()
    context = {'products':products}

    return render(request, 'home.html',context)
    

# for blank url
def index(request):
    return render(request,"index.html")

