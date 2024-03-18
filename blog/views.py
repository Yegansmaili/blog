# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from .models import *


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-updated_at')


class PostDetailView(generic.DetailView):
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    model = Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk).count()
    context = {
        'post': post,
        'cm': comments,
    }
    return render(request, 'blog/post_detail.html', context)


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    template_name = 'blog/post_create.html'
    context_object_name = 'form'
    model = Post
    form_class = PostForm  # or fields


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')

# def post_list_view(request):
#     # posts = Post.objects.all()
#     posts = Post.objects.filter(status='pub').order_by('-updated_at')
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/posts_list.html', context)
# def post_detail_view(request, pk):
#     # try:
#     post = get_object_or_404(Post, pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#
#     return render(request, 'blog/post_detail.html', {'post': post})
# def post_create_view(request):
#     if request.method == 'POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('posts_list')
#             # post_form=PostForm()
#     else:
#         post_form = PostForm()
#
#     return render(request, 'blog/post_create.html', context={'form': post_form})
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     update_form = PostForm(request.POST or None, instance=post)
#     if update_form.is_valid():
#         update_form.save()
#         return redirect('post_detail', pk=post.pk)
#     return render(request, 'blog/post_create.html', context={'form': update_form})
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', {'post': post})
