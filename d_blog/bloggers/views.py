from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import RegisterForm,PostForm



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

def login_blogger(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Welcome")
            return redirect('blogger_home')
        else:
            messages.error(request,"There was an error logging in.")
            return redirect('login_blogger')
    else:
        return render(request,'login_blogger.html')



def logout_blogger(request):
    logout(request)
    messages.success(request,"You have been logged out.")
    return render(request,'home.html')


def register_blogger(request):
    form=RegisterForm
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            # Log the user in
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('home')
        else:
            # If it was not successful tell the user something
            messages.error(request, "Registration failed. Please check your inputs.")
            return redirect('register')
    else:
        return render(request, 'register.html', {
        'form': form,
    })


