from django.shortcuts import render

def tech_blogs(request):
	return render(request, 'blogs/tech_blogs.html')
