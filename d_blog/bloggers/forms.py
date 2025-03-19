from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control'})
    )
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))

    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
