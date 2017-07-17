from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'aria-describedby': 'srnm'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type again'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'myemail@example.com'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'maxlength': '200', 'placeholder': 'https://www...'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '30', 'placeholder': 'South Pole, Moon.'}))
    date_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': 'YYYY-MM-DD'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'maxlength': '200', 'rows': 3, 'placeholder': 'Hi! Im a Gamer...'}))    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'website', 'location', 'date_birth', 'bio')

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password1')
