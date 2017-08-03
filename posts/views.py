from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment

# External Models
from userprofile.models import Connection

# Forms
from .forms import PostForm, CommentForm

class TimelineGlobalListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'timeline/timeline_global.html'

    def get_context_data(self, **kwargs):
        context = super(TimelineGlobalListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all().order_by('?')[:3]
        return context

class TimelineListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'timeline/timeline.html'

    def get_context_data(self, **kwargs):
        context = super(TimelineListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all().order_by('?')[:3]
        return context

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    success_url = reverse_lazy('timeline')
    template_name = 'posts/post_new.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('timeline')

class PostDetailView(generic.DetailView):
    model = Post
    slug_field = 'post_id'
    success_url = reverse_lazy('timeline')

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id).select_related()
        return context

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('timeline')

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('timeline')
        return super(PostDeleteView, self).dispatch(request, *args, **kwargs)

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    slug_field = 'post_id'
    form_class = CommentForm
    template_name = 'posts/comment_new.html'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()        
        return redirect('post_detail', pk=obj.post.id)