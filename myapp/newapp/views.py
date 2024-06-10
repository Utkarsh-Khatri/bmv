from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import hall,garden,pool,community_hall

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"home.html")
def SaveEnquiry(request):
    if request.method == 'POST':
        uname=request.POST.get('cust_name')
        email=request.POST.get('cust_email')
        password1=request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('The password donot match with each other try again')
        
        phone=request.POST.get('phn_no')
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken. Please choose a different username.", status=400)
        else:
            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')
    return render(request,"SignUp.html")
    
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(username,pass1)
        user = authenticate(request, username=username, password=pass1)

        print(user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            return HttpResponse('Username or Password is incorrect')
    return render(request, 'login.html',)
def homea(request):
    products = hall.objects.all()
    context = {'products':products}

    return render(request, 'home.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('login')



# for blank url
def index(request):
    return render(request,"index.html")

from django.shortcuts import render
from .models import hall, garden, pool, community_hall

def listing(request):
    hall_list = hall.objects.all()
    garden_list = garden.objects.all()
    pool_list = pool.objects.all()
    community_hall_list = community_hall.objects.all()

    if request.method == 'POST':
        selected_cap = request.POST.get('cap')
        selected_place = request.POST.get('place')
        selected_type = request.POST.get('venue')

        # Filter halls based on selected capacity, type, and city
        if selected_cap == '1':
            hall_list = hall.objects.filter(capacity__lt=1000)
        elif selected_cap == '2':
            hall_list = hall.objects.filter(capacity__range=(1000, 2000))
        elif selected_cap == '3':
            hall_list = hall.objects.filter(capacity__range=(2000, 3000))
        elif selected_cap == '4':
            hall_list = hall.objects.filter(capacity__range=(3000, 4000))
        elif selected_cap == '5':
            hall_list = hall.objects.filter(capacity__range=(4000, 5000))
        elif selected_cap == '6':
            hall_list = hall.objects.filter(capacity__gt=5000)
        else:
            hall_list = hall.objects.all()

        if selected_place:
            hall_list = hall_list.filter(city=selected_place)

        if selected_type and selected_type != 'Select Type of Venue':
            hall_list = hall_list.filter(type=selected_type)

        # Filter gardens based on selected capacity, type, and city
        if selected_cap == '1':
            garden_list = garden.objects.filter(capacity__lt=1000)
        elif selected_cap == '2':
            garden_list = garden.objects.filter(capacity__range=(1000, 2000))
        elif selected_cap == '3':
            garden_list = garden.objects.filter(capacity__range=(2000, 3000))
        elif selected_cap == '4':
            garden_list = garden.objects.filter(capacity__range=(3000, 4000))
        elif selected_cap == '5':
            garden_list = garden.objects.filter(capacity__range=(4000, 5000))
        elif selected_cap == '6':
            garden_list = garden.objects.filter(capacity__gt=5000)
        else:
            garden_list = garden.objects.all()

        if selected_place:
            garden_list = garden_list.filter(city=selected_place)

        if selected_type and selected_type != 'Select Type of Venue':
            garden_list = garden_list.filter(type=selected_type)

        # Filter pools based on selected capacity, type, and city
        if selected_cap == '1':
            pool_list = pool.objects.filter(capacity__lt=1000)
        elif selected_cap == '2':
            pool_list = pool.objects.filter(capacity__range=(1000, 2000))
        elif selected_cap == '3':
            pool_list = pool.objects.filter(capacity__range=(2000, 3000))
        elif selected_cap == '4':
            pool_list = pool.objects.filter(capacity__range=(3000, 4000))
        elif selected_cap == '5':
            pool_list = pool.objects.filter(capacity__range=(4000, 5000))
        elif selected_cap == '6':
            pool_list = pool.objects.filter(capacity__gt=5000)
        else:
            pool_list = pool.objects.all()

        if selected_place:
            pool_list = pool_list.filter(city=selected_place)

        if selected_type and selected_type != 'Select Type of Venue':
            pool_list = pool_list.filter(type=selected_type)

        # Filter community halls based on selected capacity, type, and city
        if selected_cap == '1':
            community_hall_list = community_hall.objects.filter(capacity__lt=1000)
        elif selected_cap == '2':
            community_hall_list = community_hall.objects.filter(capacity__range=(1000, 2000))
        elif selected_cap == '3':
            community_hall_list = community_hall.objects.filter(capacity__range=(2000, 3000))
        elif selected_cap == '4':
            community_hall_list = community_hall.objects.filter(capacity__range=(3000, 4000))
        elif selected_cap == '5':
            community_hall_list = community_hall.objects.filter(capacity__range=(4000, 5000))
        elif selected_cap == '6':
            community_hall_list = community_hall.objects.filter(capacity__gt=5000)
        else:
            community_hall_list = community_hall.objects.all()

        if selected_place:
            community_hall_list = community_hall_list.filter(city=selected_place)

        if selected_type and selected_type != 'Select Type of Venue':
            community_hall_list = community_hall_list.filter(type=selected_type)

    return render(request, 'home.html', {'hall_list': hall_list, 'garden_list': garden_list, 'pool_list': pool_list, 'community_hall_list': community_hall_list})
