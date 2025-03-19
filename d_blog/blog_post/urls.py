from django.urls import path
from .views import Home, Details, AddPost,UpdatePost,DeletePost


urlpatterns = [
    path('', Home.as_view(), name="blogger_home"),
    path("article/<int:pk>/",Details.as_view(), name='details'),
    path("post/",AddPost.as_view(), name='add_post'),
    path("article/edit<int:pk>/",UpdatePost.as_view(), name='update'),
    path("article/delete<int:pk>/",DeletePost.as_view(), name='delete'),

]