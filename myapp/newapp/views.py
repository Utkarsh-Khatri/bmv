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
        selected_place = request.POST.get('place')
        selected_type = request.POST.get('type')
        selected_cap = request.POST.get('cap')
        if selected_cap == '1':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity<1000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity<1000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity<1000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity<1000')
        elif selected_cap == '2':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity BETWEEN 1000 AND 2000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity BETWEEN 1000 AND 2000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity BETWEEN 1000 AND 2000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity BETWEEN 1000 AND 2000')
        elif selected_cap == '3':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity BETWEEN 2000 AND 3000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity BETWEEN 2000 AND 3000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity BETWEEN 2000 AND 3000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity BETWEEN 2000 AND 3000')
        elif selected_cap == '4':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity BETWEEN 3000 AND 4000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity BETWEEN 3000 AND 4000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity BETWEEN 3000 AND 4000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity BETWEEN 3000 AND 4000')
        elif selected_cap == '5':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity BETWEEN 4000 AND 5000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity BETWEEN 4000 AND 5000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity BETWEEN 4000 AND 5000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity BETWEEN 4000 AND 5000')
        elif selected_cap == '6':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE capacity>5000')
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE capacity>5000')
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE capacity>5000')
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE capacity>5000')

        if selected_type == 'hall' and selected_cap == '1':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity<1000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'hall' and selected_cap == '2':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity BETWEEN 1000 AND 2000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'hall' and selected_cap == '3':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity BETWEEN 2000 AND 3000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'hall' and selected_cap == '4':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity BETWEEN 3000 AND 4000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'hall' and selected_cap == '5':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity BETWEEN 4000 AND 5000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'hall' and selected_cap == '6':
            hall_list = hall.objects.raw(
                'SELECT * FROM hall WHERE city=%s AND capacity>5000', [selected_place])
            garden_list = {}
            pool_list = {}
            community_hall_list = {}

        if selected_type == 'garden' and selected_cap == '1':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity<1000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'garden' and selected_cap == '2':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity BETWEEN 1000 AND 2000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'garden' and selected_cap == '3':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity BETWEEN 2000 AND 3000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'garden' and selected_cap == '4':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity BETWEEN 3000 AND 4000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'garden' and selected_cap == '5':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity BETWEEN 4000 AND 5000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}
        elif selected_type == 'garden' and selected_cap == '6':
            garden_list = garden.objects.raw(
                'SELECT * FROM garden WHERE city=%s AND capacity>5000', [selected_place])
            hall_list = {}
            pool_list = {}
            community_hall_list = {}

        if selected_type == 'pool' and selected_cap == '1':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity<1000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}
        elif selected_type == 'pool' and selected_cap == '2':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity BETWEEN 1000 AND 2000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}
        elif selected_type == 'pool' and selected_cap == '3':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity BETWEEN 2000 AND 3000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}
        elif selected_type == 'pool' and selected_cap == '4':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity BETWEEN 3000 AND 4000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}
        elif selected_type == 'pool' and selected_cap == '5':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity BETWEEN 4000 AND 5000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}
        elif selected_type == 'pool' and selected_cap == '6':
            pool_list = pool.objects.raw(
                'SELECT * FROM pool WHERE city=%s AND capacity>5000', [selected_place])
            hall_list = {}
            garden_list = {}
            community_hall_list = {}

        if selected_type == 'community_hall' and selected_cap == '1':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity<1000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}
        elif selected_type == 'community_hall' and selected_cap == '2':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity BETWEEN 1000 AND 2000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}
        elif selected_type == 'community_hall' and selected_cap == '3':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity BETWEEN 2000 AND 3000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}
        elif selected_type == 'community_hall' and selected_cap == '4':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity BETWEEN 3000 AND 4000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}
        elif selected_type == 'community_hall' and selected_cap == '5':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity BETWEEN 4000 AND 5000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}
        elif selected_type == 'community_hall' and selected_cap == '6':
            community_hall_list = community_hall.objects.raw(
                'SELECT * FROM community_hall WHERE city=%s AND capacity>5000', [selected_place])
            hall_list = {}
            garden_list = {}
            pool_list = {}

    return render(request, 'home.html', {'hall_list': hall_list, 'garden_list': garden_list, 'pool_list': pool_list, 'community_hall_list': community_hall_list})


# BOOKING VENUE
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

def Register_Venue(request):
    flex_radio_default = request.GET.get('flexRadioDefault')
    return render(request,"list.html")