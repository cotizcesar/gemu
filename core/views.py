from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import TemplateView

# External Models
from posts.models import Post

class IndexTemplateView(generic.TemplateView):
    """
    Index shows posts, last users.
    """
    model = Post
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        context['users'] = User.objects.all()[:5]
        return context