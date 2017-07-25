from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

# External Models
from posts.models import Post

# Internal Models
from .models import Connection, UserProfile

#Forms ()
from .forms import UserForm, UserProfileForm

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    This view is for editing only the User model.
    """
    model = User
    form_class = UserForm
    template_name = 'userprofile/userprofile_edit_basic.html'
    success_url = reverse_lazy('userprofile')

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    This view is for editing only the UserProfile model.
    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userprofile/userprofile_edit_extra.html'
    success_url = reverse_lazy('timeline')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('timeline')

    def get_object(self):
        return self.request.user.userprofile

class UserProfileDetailView(generic.DetailView):
    model = User
    slug_field = 'username'
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
