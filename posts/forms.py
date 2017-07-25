from django import forms

# Models
from .models import Post, Comment

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What are you thinking?', 'maxlength': '200', 'rows': '3'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False)
    video = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Youtube, Twitch.tv, Vimeo urls.', 'aria-describedby': 'srnm'}), required=False)

    class Meta:
        model = Post
        fields = ('text', 'image', 'video')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What are you thinking?', 'maxlength': '200', 'rows': '3'}))

    class Meta:
        model = Comment
        fields = ('text',)