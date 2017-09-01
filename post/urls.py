from django.conf.urls import url

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(),  name='list_view'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail_view'),
    url(r'^create/$', PostCreateView.as_view(), name='create_view'),
]
