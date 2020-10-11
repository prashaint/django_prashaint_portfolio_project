
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import ListView, DetailView, UpdateBlogView, HomeView

app_name = 'blogs'

urlpatterns = [
    path('', HomeView.as_view(), name='tech_blogs'),
    path('curr_user_blogs/', views.curr_user_blogs, name="curr_user_blogs"),
    path('<int:blog_id>/', views.details, name='details'),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('new_blog_post/', views.new_blog_post, name="new_blog_post"),
    path('curr_user_blogs/<int:pk>', UpdateBlogView.as_view(), name='update_blog_post'),
]
