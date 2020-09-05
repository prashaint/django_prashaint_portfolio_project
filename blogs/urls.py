
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.tech_blogs, name='tech_blogs'),
    path('<int:blog_id>/', views.details, name='details'),
    #path('portfolio/', include('portfolio.urls')),
]
