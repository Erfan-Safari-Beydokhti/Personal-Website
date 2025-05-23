from django import forms
from .models import ContactMessage,AboutMe

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']

class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['name','bio','profile_picture','skills']

