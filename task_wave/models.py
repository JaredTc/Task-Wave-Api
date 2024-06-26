from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    dateEnd = models.DateField()
    assigned_to = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField()
    is_completed = models.BooleanField(default=False)
    alerts = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100)
    objective = models.TextField()
    porcent = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    position = models.CharField(max_length=255, blank=True, null=True)
    imgProfile = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


