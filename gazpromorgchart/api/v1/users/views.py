from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from core.users.models import Users
from .serializers import UsersSerializer, UsersLimitedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """Вьюсет для CRUD запросов к модели Users с ограниченным набором полей"""
    queryset = Users.objects.all()
    serializer_class = UsersLimitedSerializer
    operation_description = "Получение списка пользователей и создание нового пользователя"

class UserMeView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения и редактирования данных текущего пользователя"""
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    operation_description = "Получение, обновление и удаление данных текущего пользователя"

    def get_object(self):
        return self.request.user.users

class UserDetailView(generics.RetrieveAPIView):
    """Вьюсет для получения данных другого пользователя по ID"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'pk'
    operation_description = "Получение данных пользователя по ID"