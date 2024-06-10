from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hall(models.Model):
    hall_id= models.AutoField(primary_key=True)
    venue_type = models.CharField(max_length=100, default = 'Hall')
    hall_name= models.CharField(max_length=500)
    city= models.CharField(max_length=500)
    locality=models.CharField(max_length=500)
    description=models.CharField(max_length=1500)
    contact_no=models.CharField(max_length=500)
    capacity=models.PositiveIntegerField()
    url=models.CharField(max_length=500)
    manager_name=models.CharField(max_length=500)
    hall_email_id=models.CharField(max_length=500)
    cost=models.PositiveIntegerField()  
    img=models.ImageField(upload_to='Photos/') 

class garden(models.Model):
    garden_id= models.AutoField(primary_key=True)
    venue_type = models.CharField(max_length=100, default = 'Garden')
    garden_name= models.CharField(max_length=1500)
    city= models.CharField(max_length=500)
    locality=models.CharField(max_length=500)
    description=models.CharField(max_length=1500)
    contact_no=models.CharField(max_length=500)
    capacity=models.PositiveIntegerField()
    url=models.CharField(max_length=500)
    manager_name=models.CharField(max_length=500)
    garden_email_id=models.CharField(max_length=500)
    cost=models.PositiveIntegerField()
    img=models.ImageField(upload_to='Photos/')

class community_hall(models.Model):
    community_hall_id= models.AutoField(primary_key=True)
    venue_type = models.CharField(max_length=100, default ="CommunityHall")
    community_hall_name= models.CharField(max_length=500)
    city= models.CharField(max_length=500)
    locality=models.CharField(max_length=500)
    description=models.CharField(max_length=1500)
    contact_no=models.CharField(max_length=500)
    capacity=models.PositiveIntegerField()
    url=models.CharField(max_length=500)
    manager_name=models.CharField(max_length=500)
    community_hall_email_id=models.CharField(max_length=500)
    cost=models.PositiveIntegerField()
    img=models.ImageField(upload_to='Photos/')  

class pool(models.Model):
    pool_id= models.AutoField(primary_key=True)
    venue_type = models.CharField(max_length=100, default = 'Pool')
    pool_name= models.CharField(max_length=500)
    city= models.CharField(max_length=500)
    locality=models.CharField(max_length=500)
    description=models.CharField(max_length=1500)
    contact_no=models.CharField(max_length=500)
    capacity=models.PositiveIntegerField()
    url=models.CharField(max_length=500)
    manager_name=models.CharField(max_length=500)
    pool_email_id=models.CharField(max_length=500)
    cost=models.PositiveIntegerField() 
    img=models.ImageField(upload_to='Photos/')

# for booking halls 
class Booking(models.Model):
    vname = models.CharField(max_length=100, default = 'Venue')
    custn = models.CharField(max_length=100, default = 'Unknown')
    phn = models.CharField(max_length=15, default = '')
    email = models.EmailField(default = '')
    addr = models.TextField(default = '')
    booking_date = models.DateField()

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.venue_name} on {self.booking_date}"
