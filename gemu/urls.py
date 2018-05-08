"""gemu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url

from core.views import Index, PublicTimeline, ExploreUsers, UserUpdateView, UserProfileUpdateView, UserProfileDetailView, PostCreateView, PostDetailView, CommentCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    # Timelines: Public, Following, Etc.
    url(r'^timeline/public$', PublicTimeline.as_view(), name='timeline_public'),
    url(r'^explore/$', ExploreUsers.as_view(), name='explore_users'),
    # django-allauth: All url patterns
    # http://django-allauth.readthedocs.io/en/latest/installation.html#django
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/basic/$', UserUpdateView.as_view(), name='userprofile_basic'),
    url(r'^accounts/advanced/$', UserProfileUpdateView.as_view(), name='userprofile_advanced'),
    url(r'^user/(?P<slug>[a-zA-Z0-9]+)/$', UserProfileDetailView.as_view(), name='userprofile'),
    # Post: CRUD url's.
    url(r'^post/create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    # Post Comments: CRUD url's.
    url(r'^post/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='post_comment_create'),
    # django-activity-stream: Testing URL
    url('^activity/', include('actstream.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)