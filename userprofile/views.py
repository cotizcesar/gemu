from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# External Models
from posts.models import Post

# Internal Models
from .models import Connection, UserProfile

#Forms
from .forms import UserForm, UserProfileForm

class UserProfileDetailView(generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'perfil/perfil.html'
    context_object_name = 'usr'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.get_object())
        context['follower'] = Connection.objects.filter(follower=self.get_object())
        context['following'] = Connection.objects.filter(following=self.get_object())
        return context

class FollowingDetailView(generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'connection/profile_following.html'

    def following(self):
        return Connection.objects.filter(following=self.get_object())

class FollowerDetailView(generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'connection/profile_follower.html'

    def followers(self):
        return Connection.objects.filter(follower=self.get_object())

class UserProfileUpdateView(generic.UpdateView):
    model = User
    second_model = UserProfile
    slug_field = 'username'
    form_class = UserForm
    second_form_class = UserProfileForm
    template_name = 'perfil/profile_edit.html'