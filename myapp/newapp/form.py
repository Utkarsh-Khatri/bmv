from django import forms
from .models import hall

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'address', 'phone', 'image']
