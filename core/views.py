from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages

# Django: Importing User Model
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

# Core: Importing Post Model
from .models import Post, Comment, UProfile

# Core: Importing PostForm form
from .forms import UserForm, UProfileForm, PostForm, CommentForm

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('?')[:3]
        context['public_posts'] = Post.objects.all()
        context['index_posts'] = Post.objects.all()[:3]
        context['users_count'] = User.objects.all().count
        context['posts_count'] = Post.objects.all().count
        return context

class PublicTimeline(TemplateView):
    template_name = 'timeline/timeline_public.html'

    def get_context_data(self, **kwargs):
        context = super(PublicTimeline, self).get_context_data(**kwargs)
        context['public_timeline'] = Post.objects.all()
        return context

class Explore(TemplateView):
    template_name = 'explore/explore.html'

    def get_context_data(self, **kwargs):
        context = super(Explore, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.count
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'uprofile/uprofile_update_basic.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class UProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UProfile
    form_class = UProfileForm
    template_name = 'uprofile/uprofile_update_advanced.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UProfileUpdateView, self).form_valid(form)

    def get_object(self):
        return self.request.user.uprofile

# UProfile: Detail view of the extension user profile.
class UProfileDetailView(DetailView):
    model = User
    template_name = 'uprofile/uprofile.html'
    slug_field = 'username'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UProfileDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.get_object())
        context['users'] = User.objects.all().order_by('?')[:3]
        return context

# Post: Just a post creation.
class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    success_url = reverse_lazy('index')
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('index')

# Post: a Detail view of every post.
class PostDetailView(DetailView):
    model = Post
    slug_field = 'post_id'
    success_url = reverse_lazy('index')
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id).select_related()
        return context

# Comment: A Comment creation linked to a Post.
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    slug_field = 'post_id'
    form_class = CommentForm
    template_name = 'post/post_comment_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()        
        return redirect('post_detail', pk=obj.post.id)