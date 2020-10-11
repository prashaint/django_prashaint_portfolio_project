from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views import generic
from django.forms import ModelForm
from .forms import BlogPostForm
from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse

class HomeView(ListView):
	model = BlogPost
	template_name = 'blogs/tech_blogs.html'

class UpdateBlogView(UpdateView):
	model = BlogPost
	template_name = 'blogs/update_blog_post.html'
	fields = [ 'title', 'content' ]
		
	def get_success_url(self):
		return reverse('blogs:curr_user_blogs')

class DeletePostView(DeleteView):
	model = BlogPost
	template_name = 'blogs/delete_post.html'

	def get_success_url(self):
		return reverse('blogs:curr_user_blogs')

class BlogPostForm(ModelForm):
	class Meta:
		model = BlogPost
		form_class = BlogPostForm
		fields = '__all__'

def new_blog_post(request):
	if request.method == 'GET':
		return render(request, 'blogs/new_blog_post.html', {'form':BlogPostForm()})
	else:
		if request.method == 'POST':
			new_blog = BlogPost()
			new_post_form = BlogPostForm(request.POST, instance=new_blog)
			new_post = new_post_form.save()
			return redirect('blogs:curr_user_blogs')
		else:
			return render(request, 'blogs/new_blog_post.html', {'form':BlogPostForm()})

def tech_blogs(request):
	blogs = BlogPost.objects.filter(status=1).order_by('-created_on')
	return render(request, 'blogs/tech_blogs.html', {'blogs':blogs})

def details(request, blog_id):
	blog = get_object_or_404(BlogPost, pk=blog_id)
	return render(request, 'blogs/details.html', {'blog':blog})

def curr_user_blogs(request):
	blogs = BlogPost.objects.all()
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
				return redirect('blogs:curr_user_blogs')
			except IntegrityError:
				return render(request, 'blogs/user_signup.html', {'form':UserCreationForm(), 'error':'Username already exists. Please choose another name.'})
		else:
			return render(request, 'blogs/user_signup.html', {'form':UserCreationForm(), 'error':'Password and Confirmation Password did not match.'})

def user_login(request):
	if request.method == 'GET': 
		return render(request, 'blogs/user_login.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'blogs/user_login.html', {'form':AuthenticationForm(), 'error':'Username or Password did not match'})
		else:
			login(request, user)
			return redirect('blogs:curr_user_blogs')

def user_logout(request):
	if request.method == 'POST':
		logout(request)
		return render(request, 'blogs/user_logout.html')






