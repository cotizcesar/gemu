from django import forms
from django.contrib.auth.models import User

# External Models
from .models import UserProfile, Connection

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'aria-describedby': 'srnm'}))
    password1 = forms.CharField(required = False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required = False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type again'}))
    email = forms.CharField(required = False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'myemail@example.com'}))   

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')

class UserProfileForm(forms.ModelForm):
    header = forms.ImageField(required = False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required = False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    website = forms.CharField(required = False, widget=forms.URLInput(attrs={'class': 'form-control', 'maxlength': '200', 'placeholder': 'https://www...'}))
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '30', 'placeholder': 'South Pole, Moon.'}))
    date_birth = forms.CharField(required = False, widget=forms.DateInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': 'YYYY-MM-DD'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'maxlength': '200', 'placeholder': 'Hi! Im a Gamer...'}))    

    class Meta:
        model = UserProfile
        fields = ('avatar', 'header', 'website', 'location', 'date_birth', 'bio')