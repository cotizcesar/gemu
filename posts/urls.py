from django.conf.urls import include, url

# My custom CBV
from .views import TimelineListView, TimelineGlobalListView, PostCreateView, PostDetailView, PostDeleteView, CommentCreateView

urlpatterns = [
    url(r'^user/$', TimelineListView.as_view(), name='timeline'),
    url(r'^global/$', TimelineGlobalListView.as_view(), name='timeline_global'),
    url(r'^p/new$', PostCreateView.as_view(), name='post_new'),
    url(r'^p/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    url(r'^p/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='post_comment'),
    #url(r'^p/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='post_comment'),
    url(r'^p/delete/(?P<pk>\d+)$', PostDeleteView.as_view(), name='post_delete'),
]