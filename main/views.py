from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'title': 'Main page',
    }
    return render(request, 'main/index.html', context)