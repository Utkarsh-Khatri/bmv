from django import forms
from .models import hall
from .models import Booking

# class VenueForm(forms.ModelForm):
#     class Meta:
#         model = Venue
#         fields = ['venue_name', 'address', 'phone', 'image']

from django import forms
from .models import Booking

class VenueBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['venue_name', 'venue_type', 'date_start', 'date_end', 'requirements', 'customer_name', 'phone_number', 'email', 'address']
