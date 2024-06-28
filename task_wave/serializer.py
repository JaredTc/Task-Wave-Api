from django.contrib.auth.models import User
from rest_framework import serializers

from task_wave.models import CustomUser, Task


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'password',
            'email',
            'is_staff',
            'is_active',
            'position',
            'imgProfile'

        ]

    def create(self, validated_data):
        imgProfile = validated_data.pop('imgProfile', '')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff'],
            is_active=validated_data['is_active'],
            email=validated_data['email'],
            position=validated_data['position'],
            imgProfile=imgProfile

        )
        return user




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'password',
            'email',
            'is_staff',
            'is_active',
            'position',
            'imgProfile',
        ]



class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'position',
            'imgProfile',
        ]
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.position = validated_data.get('position', instance.position)
        instance.imgProfile = validated_data.get('imgProfile', instance.imgProfile)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'dateEnd',
            'assigned_to',
            'description',
            'category',
            'status',
            'is_completed',
            'alerts',
            'created_by',
            'objective',
            'porcent',
        ]

    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data['title'],
            dateEnd=validated_data['dateEnd'],
            assigned_to=validated_data['assigned_to'],
            description=validated_data['description'],
            category=validated_data['category'],
            status=validated_data['status'],
            is_completed=validated_data['is_completed'],
            alerts=validated_data['alerts'],
            created_by=validated_data['created_by'],
            objective=validated_data['objective'],
            porcent=validated_data['porcent']
        )
        return task


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'dateEnd',
            'assigned_to',
            'description',
            'category',
            'status',
            'is_completed',
            'alerts',
            'created_by',
            'objective',
            'porcent',
            "created_at",
            "updated_at"
        ]