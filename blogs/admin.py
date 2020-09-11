from django.contrib import admin
from .models import BlogPost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    #prepopulated_fields = {(title:'title')}

admin.site.register(BlogPost, BlogAdmin)

