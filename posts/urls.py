from django.conf.urls import include, url

from .views import TimelineListView, TimelineGlobalListView, PostCreateView, PostDetailView, PostDeleteView

urlpatterns = [
    url(r'^user/$', TimelineGlobalListView.as_view(), name='timeline'),
    url(r'^global/$', TimelineGlobalListView.as_view(), name='timeline_global'),
    url(r'^post/new$', PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/delete/(?P<pk>\d+)$', PostDeleteView.as_view(), name='post_delete'),
]