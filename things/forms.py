"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),  # Customize textarea size
            'quantity': forms.NumberInput(attrs={'min': 1}),  # Set minimum value for quantity
        }

