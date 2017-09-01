from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    template_name = 'post/create.html'
    fields = ['title', 'content']

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        message = 'Post successfully created.'
        messages.success(self.request, message)
        return super(PostCreateView, self).form_valid(form)



