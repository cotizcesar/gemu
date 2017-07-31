from django.conf.urls import include, url

from .views import TimelineListView, TimelineGlobalListView, PostCreateView, PostDetailView, PostDeleteView

urlpatterns = [
    url(r'^user/$', TimelineListView.as_view(), name='timeline'),
    url(r'^global/$', TimelineGlobalListView.as_view(), name='timeline_global'),
    url(r'^p/new$', PostCreateView.as_view(), name='post_new'),
    url(r'^p/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^p/delete/(?P<pk>\d+)$', PostDeleteView.as_view(), name='post_delete'),
]