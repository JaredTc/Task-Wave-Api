from django.urls import path
from .views import Hello, LoginView, UserRegistrationView, UserListView, UpdateUserView, DeleteUserView, UserInfoView

urlpatterns = [
    path('hello/', Hello.as_view(), name='hello'),
    path('auth-user', LoginView.as_view(), name='login'),
    path('register-user', UserRegistrationView.as_view(), name='register'),
    path('users', UserListView.as_view(), name='users'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='update-user'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(), name='delete-user'),
    path('view-user/<int:pk>', UserInfoView.as_view(), name='view-user'),
]