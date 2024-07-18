from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', BlogDisplay.as_view(), name='post'),
    path('home/', HomePageView.as_view(), name='home'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', NewPostView.as_view(), name='post_new'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
