from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

# External Models
from posts.models import Post

# Forms
from .forms import SignUpForm

class IndexTemplateView(generic.TemplateView):
    model = Post
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        context['users'] = User.objects.all()[:5]
        return context

# Signup https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-profile-model
def signup(request):
    if request.user.is_authenticated():
        return redirect('timeline')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.userprofile.bio = form.cleaned_data.get('bio')
            user.userprofile.website = form.cleaned_data.get('website')
            user.userprofile.location = form.cleaned_data.get('location')
            user.userprofile.date_birth = form.cleaned_data.get('date_birth')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('timeline')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})