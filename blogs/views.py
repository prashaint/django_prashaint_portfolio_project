from django.shortcuts import render, get_object_or_404
from .models import Blog

def tech_blogs(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/tech_blogs.html', {'blogs':blogs})

def details(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/details.html', {'blog':blog})

