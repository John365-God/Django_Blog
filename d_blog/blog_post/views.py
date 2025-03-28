from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .models import Post, Comments
from .forms import PostForm,CommentForm
import random

# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']
    paginate_by = 6  # Display 5 posts per page

class Details(DetailView):
    model = Post
    template_name = 'details.html'
    #To get the current page so the viewer can go to it after reading the details instead of the homepage.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the 'next' parameter from the GET request, which will hold the current page
        context['next_page'] = self.request.GET.get('next', None)
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # No need to specify 'author' in the fields, as it's handled automatically via the hidden input
    def form_valid(self, form):
        # Ensure that the 'author' is set automatically based on the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the 'next' parameter from the GET request, which will hold the current page
        context['next_page'] = self.request.GET.get('next', None)

        return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blogger_home')  # Default redirect after deletion

    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)

        # Get the 'next' parameter from the GET request, which will hold the current page
        context['next_page'] = self.request.GET.get('next', self.success_url)

        return context


class AddComment(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('blogger_home')

    def form_valid(self, form):
        # Set the 'name' field to the logged-in user's name automatically
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


