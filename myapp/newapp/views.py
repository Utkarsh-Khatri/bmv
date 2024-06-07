from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world")
def SaveEnquiry(request):
    return render(request, "SignUp.html")

