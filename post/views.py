from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/list.html'
    paginate_by = 3


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    template_name = 'post/update.html'
    fields = ['title', 'content']

    def get_form(self, form_class=None):
        form = super(PostUpdateView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        return form

    def form_valid(self, form):
        message = 'Post successfully changed.'
        messages.success(self.request, message)
        return super(PostUpdateView, self).form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    template_name = 'post/delete.html'

    def delete(self, request, *args, **kwargs):
        message = 'Post successfully deleted.'
        messages.success(self.request, message)
        return super(PostDeleteView, self).delete(self, request, *args,
                                                  **kwargs)


