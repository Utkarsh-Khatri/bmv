from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import hall,garden,pool,community_hall

# Create your views here.
def home(request):
    return HttpResponse("Hello world")
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
