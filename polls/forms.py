from logging import PlaceHolder
from django import forms
from polls.models import Sign

class SignForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label="")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="")
        
    class Meta():
        model = Sign
        fields = ["email", "password"]