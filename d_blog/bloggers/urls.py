from . import views
from django.urls import path

urlpatterns = [
    path('login_blogger/', views.login_user, name='login'),
    path('logout_blogger/', views.logout_user, name='logout'),
    path('register_blogger/', views.register_user, name='register'),
]