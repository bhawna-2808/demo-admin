from .models import *
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-alternative'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-alternative'}),
        }

       
        
        
        