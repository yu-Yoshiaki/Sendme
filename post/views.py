from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
"""
class indexListView(generic.ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
"""

class index(generic.TemplateView):
    template_name = "post/index.html"
