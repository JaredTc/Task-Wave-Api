from django.urls import path

from .Task.views import GetTaskView, CreateTask
from .views import Hello, LoginView, UserRegistrationView, UserListView, UpdateUserView, DeleteUserView, UserInfoView, \
    HelloLinux

urlpatterns = [
    path('hello/', Hello.as_view(), name='hello'),
    path('auth-user/', LoginView.as_view(), name='login'),
    path('register-user', UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='update-user'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(), name='delete-user'),
    path('view-user/<int:pk>', UserInfoView.as_view(), name='view-user'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('task-list/', GetTaskView.as_view(), name='task-list'),
    path('hello-linux/', HelloLinux.as_view(), name='hello-linux'),
]