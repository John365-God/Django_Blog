from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .models import Post
from .forms import PostForm
from django.views.generic import ListView

# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']
    paginate_by = 6  # Display 5 posts per page

class Details(DetailView):
    model = Post
    template_name = 'details.html'

class AddPost(CreateView):
    model = Post
    form_class=PostForm
    template_name = 'add_post.html'
    # fields = 'title','content','author'

class UpdatePost(UpdateView):
    model= Post
    template_name = 'update_post.html'
    fields = 'title','content'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blogger_home')

