from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm



# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']
    # ordering = ['-id'] The ordering sets how the posts are ordered. It's negative to put the latest blog first.

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

