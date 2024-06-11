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
        fields = ['user_name', 'user_contact', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }
