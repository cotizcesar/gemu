from django.conf.urls import url

from .views import UserProfileDetailView, FollowerDetailView, FollowingDetailView

urlpatterns = [
    url(r'^followers/$', FollowerDetailView.as_view(), name='user_followers'),
    url(r'^following/$', FollowingDetailView.as_view(), name='user_following'),
    url(r'^$', UserProfileDetailView.as_view(), name='userprofile'),
]
