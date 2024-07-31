from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from core.users.models import Users
from .serializers import UserSerializer, UsersSerializer, UsersLimitedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """Вьюсет для CRUD запросов к модели Users с ограниченным набором полей"""
    queryset = Users.objects.all()
    serializer_class = UsersLimitedSerializer
    operation_description = "Получение списка пользователей и создание нового пользователя"

class UserMeView(generics.RetrieveUpdateDestroyAPIView):
    """Вью для получения и редактирования данных текущего пользователя"""
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    operation_description = "Получение, обновление и удаление данных текущего пользователя"

    def get_object(self):
        return self.request.user.users

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вью для получения и редактирования данных другого пользователя по ID"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'
    operation_description = "Получение, обновление и удаление данных пользователя по ID"