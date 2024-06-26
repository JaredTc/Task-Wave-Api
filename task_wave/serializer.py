from django.contrib.auth.models import User
from rest_framework import serializers

from task_wave.models import CustomUser


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

