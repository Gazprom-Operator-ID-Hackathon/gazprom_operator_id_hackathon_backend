from rest_framework import serializers
from django.contrib.auth.models import User
from core.employees.models import Employee

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сотрудника с полным набором полей"""
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeLimitedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сотрудника с ограниченным набором полей"""
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position']