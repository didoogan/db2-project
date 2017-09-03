from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Post, Comment


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/list.html'
    paginate_by = 4


# class PostDetailView(LoginRequiredMixin, DetailView):
#     model = Post
#     template_name = 'post/detail.html'


class PostDetailView(LoginRequiredMixin, View):

    @staticmethod
    def get_post(pk):
        return Post.objects.get(pk=pk)

    def get(self, request, pk):
        post = PostDetailView.get_post(pk)
        comments_list = post.comments.all()
        paginator = Paginator(comments_list, 3)

        page = request.GET.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)
        return render(request, 'post/detail.html', {'post': post,
                                                    'comments': comments})

    def post(self, request, pk):
        post = PostDetailView.get_post(pk)
        text = request.POST.get('comment', False)
        if not text:
            message = 'You should to provide a comment text.'
            messages.error(self.request, message)
            return HttpResponseRedirect('/post/{}'.format(pk))
        Comment.objects.create(author=request.user, post=post, text=text)
        message = 'Comment successfully created'
        messages.success(self.request, message)
        return HttpResponseRedirect('/post/{}'.format(pk))


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


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    template_name = 'post/delete.html'

    def delete(self, request, *args, **kwargs):
        message = 'Post successfully deleted.'
        messages.success(self.request, message)
        return super(PostDeleteView, self).delete(self, request, *args,
                                                  **kwargs)


class LikeCreateDeleteView(LoginRequiredMixin, View):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return JsonResponse({'likes': post.likes_num})

