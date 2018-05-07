from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import Post, Comment, UProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class UProfileForm(forms.ModelForm):
    class Meta:
        model = UProfile
        fields = ('avatar', 'header', 'website', 'bio')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'video')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)