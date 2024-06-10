from django import forms
from .models import hall
from .models import Booking

# class VenueForm(forms.ModelForm):
#     class Meta:
#         model = Venue
#         fields = ['venue_name', 'address', 'phone', 'image']

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['vname', 'custn', 'phn', 'email', 'addr', 'date']

    vname = forms.CharField(max_length=100, label='Enter Venue name')
    custn = forms.CharField(max_length=100, label='Enter your full name')
    phn = forms.CharField(max_length=15, label='Phone Number')
    email = forms.EmailField(label='Enter Email-id')
    addr = forms.CharField(widget=forms.Textarea, label='Enter Full Address')
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Select date and time')
    print(vname,custn,phn,email,addr,date)
