from django.shortcuts import render
from .models import *
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class BlogDisplay(ListView):
    model = Blog
    template_name = 'posts.html'
    context_object_name = 'all_posts'

class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'blog'

class NewPostView(CreateView):
    model = Blog
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']

class PostUpdateView(UpdateView):
    model = Blog
    template_name = 'edit_post.html'
    fields = ['title', 'author', 'body']

class PostDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post')