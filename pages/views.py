from django.shortcuts import render
from django.views import generic

from blog.models import *


# def home_view(request):
#     posts = Post.objects.all()[:3]
#     context = {
#         'posts': posts
#     }
#     return render(request, 'home.html', context)
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['posts'] = Post.objects.all()[:3]
        return super().get_context_data(**kwargs)
