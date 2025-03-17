from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

# class Blogger(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     password=models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # slug = models.SlugField(unique=True)
    # published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse('blogger_home')

#
# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#
#     def __str__(self):
#         return self.name
