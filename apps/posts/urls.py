from django.urls import path

from apps.posts.views import PostAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView


urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='api_posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='api_posts_detail'),
    path('posts/create/', PostCreateAPIView.as_view(), name='api_posts_create'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_posts_update'),
    path('posts/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='api_posts_delete'),
]