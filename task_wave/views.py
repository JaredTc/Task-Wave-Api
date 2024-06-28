from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError

from task_wave.models import CustomUser
from task_wave.serializer import UserRegistrationSerializer, UserSerializer, UpdateUserSerializer, TaskSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):
    """
     API endpoint for user registration.
     """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": "Something went wrong. Please try again."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @permission_classes([IsAuthenticated])
class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# permission_classes([IsAuthenticated])
class UpdateUserView(APIView):
    def put(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User update successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# permission_classes([IsAuthenticated])
class DeleteUserView(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if not request.user.is_superuser and request.user != user:
            return Response({'detail': 'No tienes permiso para realizar esta acción.'}, status=status.HTTP_403_FORBIDDEN)

        user.delete()
        return Response({'message': 'User delete successfully'},status=status.HTTP_204_NO_CONTENT)


class UserInfoView(APIView):
    # permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a esta vista

    def get(self, request,pk):
        try:
            user = CustomUser.objects.get(pk=pk)  # Obtiene el usuario por su ID
            serializer = UserSerializer(user)  # Serializa los datos del usuario
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class Hello(APIView):
    def get(self, request):
        return JsonResponse({'message': '¡Hola, mundo!'}, status=200)

class HelloLinux(APIView):
    def get(self, request):
        return JsonResponse({'message': 'Hello, Linux!'}, status=200)



