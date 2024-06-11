from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import hall,garden,pool,community_hall
from .form import BookingForm
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
            return redirect ('homea')
        else:
            return HttpResponse('Username or Password is incorrect')
    return render(request, 'login.html',)
def homea(request):
    products = hall.objects.all()
    community_halls = community_hall.objects.all()
    pools = pool.objects.all()
    gardens = garden.objects.all()
    context = {
        'products': products,
        'community_halls': community_halls,
        'pools': pools,
        'gardens': gardens,
    }

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
        selected_place = request.POST.get('place', '').strip()
        selected_type = request.POST.get('venue', '').strip()
        selected_cap = request.POST.get('cap', '').strip()

        print("Selected Place:", selected_place)
        print("Selected Type:", selected_type)
        print("Selected Capacity:", selected_cap)

        capacity_filters = {
            '1': (0, 999),
            '2': (1000, 2000),
            '3': (2001, 3000),
            '4': (3001, 4000),
            '5': (4001, 5000),
            '6': (5001, float('inf'))
        }

        if selected_cap in capacity_filters:
            min_cap, max_cap = capacity_filters[selected_cap]
            hall_list = hall_list.filter(capacity__gte=min_cap, capacity__lte=max_cap)
            garden_list = garden_list.filter(capacity__gte=min_cap, capacity__lte=max_cap)
            pool_list = pool_list.filter(capacity__gte=min_cap, capacity__lte=max_cap)
            community_hall_list = community_hall_list.filter(capacity__gte=min_cap, capacity__lte=max_cap)

            print("Filtered Hall List by Capacity:", hall_list)
            print("Filtered Garden List by Capacity:", garden_list)
            print("Filtered Pool List by Capacity:", pool_list)
            print("Filtered Community Hall List by Capacity:", community_hall_list)

        if selected_place:
            hall_list = hall_list.filter(city=selected_place)
            garden_list = garden_list.filter(city=selected_place)
            pool_list = pool_list.filter(city=selected_place)
            community_hall_list = community_hall_list.filter(city=selected_place)

            print("Filtered Hall List by City:", hall_list)
            print("Filtered Garden List by City:", garden_list)
            print("Filtered Pool List by City:", pool_list)
            print("Filtered Community Hall List by City:", community_hall_list)

        if selected_type:
            if selected_type == 'hall':
                garden_list = None
                pool_list = None
                community_hall_list = None
            elif selected_type == 'garden':
                hall_list = None
                pool_list = None
                community_hall_list = None
            elif selected_type == 'pool':
                hall_list = None
                garden_list = None
                community_hall_list = None
            elif selected_type == 'community_hall':
                hall_list = None
                garden_list = None
                pool_list = None

            print("Filtered by Type - Hall List:", hall_list)
            print("Filtered by Type - Garden List:", garden_list)
            print("Filtered by Type - Pool List:", pool_list)
            print("Filtered by Type - Community Hall List:", community_hall_list)

        context = {
            'hall_list': hall_list,
            'garden_list': garden_list,
            'pool_list': pool_list,
            'community_hall_list': community_hall_list,
        }
        
        print("Final Context:", context)
        return render(request, 'search.html', context)

    context = {
        'hall_list': hall_list,
        'garden_list': garden_list,
        'pool_list': pool_list,
        'community_hall_list': community_hall_list,
    }
    return render(request, 'search.html', context)


# BOOKING VENUE
def book(request):
    return render(request,"book.html")
@login_required
def book_venue(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})