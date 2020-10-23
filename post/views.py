from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class indexListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
