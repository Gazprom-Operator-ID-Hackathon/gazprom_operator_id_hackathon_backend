from rest_framework import viewsets, generics, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from core.users.models import Users
from .serializers import UsersSerializer, UsersLimitedSerializer, RegisterSerializer, UserSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для получения списка пользователей с ограниченным набором полей"""
    queryset = Users.objects.all()
    serializer_class = UsersLimitedSerializer
    operation_description = "Получение списка пользователей для формирования диаграммы"

class UserMeView(APIView):
    """Вьюсет для перенаправления на профиль первого пользователя"""
    def get(self, request, *args, **kwargs):
        return redirect('user-detail', pk=1)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения данных другого пользователя по ID и выполнения CRUD операций"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'pk'
    operation_description = "Получение, создание, обновление и удаление данных пользователя по ID"

class RegisterView(generics.CreateAPIView):
    """Вьюсет для регистрации нового пользователя"""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'token': token.key
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class LoginView(ObtainAuthToken):
    """Вьюсет для аутентификации пользователя"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)