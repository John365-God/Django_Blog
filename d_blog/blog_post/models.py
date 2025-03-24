from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse('blogger_home')

