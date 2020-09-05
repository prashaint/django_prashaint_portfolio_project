from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'author')
    body = models.TextField()
    created_date = models.DateTimeField(blank = True, null = True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title