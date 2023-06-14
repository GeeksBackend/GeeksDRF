from django.urls import path 

from apps.users.views import UserAPIViewSet, UserRegisterAPIView


urlpatterns = [
    path('users/', UserAPIViewSet.as_view(), name="api_users"),
    path('register/', UserRegisterAPIView.as_view(), name="api_user_register")
]