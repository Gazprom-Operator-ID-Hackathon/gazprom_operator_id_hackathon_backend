from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from core.employees.models import Employee
from .serializers import UserSerializer, EmployeeSerializer, EmployeeLimitedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """Вьюсет для CRUD запросов к модели Employee с ограниченным набором полей"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeLimitedSerializer
    operation_description = "Получение списка сотрудников и создание нового сотрудника"

class UserMeView(generics.RetrieveUpdateDestroyAPIView):
    """Вью для получения и редактирования данных текущего пользователя"""
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    operation_description = "Получение, обновление и удаление данных текущего пользователя"

    def get_object(self):
        return self.request.user.employee

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вью для получения и редактирования данных другого сотрудника по ID"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    operation_description = "Получение, обновление и удаление данных сотрудника по ID"