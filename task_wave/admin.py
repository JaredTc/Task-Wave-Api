from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Importa el modelo de usuario personalizado

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'position', 'imgProfile']  # Agrega el campo position

admin.site.register(CustomUser, CustomUserAdmin)