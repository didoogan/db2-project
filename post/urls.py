from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import PostListView, PostDetailView, PostCreateView, Post, \
    PostUpdateView, PostDeleteView, LikeCreateDeleteView

urlpatterns = [
    url(r'^$', PostListView.as_view(),  name='list_view'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail_view'),
    url(r'^(?P<pk>\d+)/like/$', csrf_exempt(LikeCreateDeleteView.as_view()), name='like'),
    url(r'^create/$', PostCreateView.as_view(), name='create_view'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(),
        name='update_view'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(),
        name='delete_view'),
]
