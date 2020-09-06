from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError

def tech_blogs(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/tech_blogs.html', {'blogs':blogs})

def details(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/details.html', {'blog':blog})

def curr_user_blogs(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/curr_user_blogs.html', {'blogs':blogs})

def user_signup(request):
	if request.method == 'GET': 
		return render(request, 'blogs/user_signup.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('curr_user_blogs')
			except IntegrityError:
				return render(request, 'blogs/user_signup.html', {'form':UserCreationForm(), 'error':'Username already exists. Please choose another name.'})
		else:
			return render(request, 'blogs/user_signup.html', {'form':UserCreationForm(), 'error':'Password and Confirmation password did not match.'})










