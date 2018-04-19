from django.shortcuts import render
from .models import Post, SECTIONS

def index(request):
    post = Post.objects.all()
    ctx = {'post': post, 'sections': SECTIONS}
    return(render(request, 'chorievsite/index.html', ctx))
