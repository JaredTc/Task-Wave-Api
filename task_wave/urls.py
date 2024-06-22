from django.urls import path
from .views import Hello, LoginView, UserRegistrationView, UserListView

urlpatterns = [
    path('hello/', Hello.as_view(), name='hello'),
    path('auth-user', LoginView.as_view(), name='login'),
    path('register-user', UserRegistrationView.as_view(), name='register'),
    path('users', UserListView.as_view(), name='users'),
]