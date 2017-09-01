from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


