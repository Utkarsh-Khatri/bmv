from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")
def SaveEnquiry(request):
    return render(request, "SignUp.html")

# for blank url
def index(request):
    return render(request,"index.html")

