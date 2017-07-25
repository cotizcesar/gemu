"""plaxed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# General Auth (Signup, Login and Logout)
from django.contrib.auth import views as auth_views
from core import views as core_views

# Views de Core
from core.views import IndexTemplateView
from core.views import UserLogin, UserLogout

# External Views
from userprofile.views import UserUpdateView, UserProfileUpdateView

urlpatterns = [
    # General Auth (Index, Signup, Login and Logout)
    url(r'^$', IndexTemplateView.as_view(), name='index'),
    url(r'^accounts/login/$', UserLogin.as_view(), name='login'),
    url(r'^accounts/logout/$', UserLogout.as_view(), name='logout'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('posts.urls')),
    url(r'^accounts/basic/$', UserUpdateView.as_view(), name='userprofile_basic'),
    url(r'^accounts/extra/$', UserProfileUpdateView.as_view(), name='userprofile_extra'),
    url(r'^u/(?P<slug>[a-zA-Z0-9]+)/', include('userprofile.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
