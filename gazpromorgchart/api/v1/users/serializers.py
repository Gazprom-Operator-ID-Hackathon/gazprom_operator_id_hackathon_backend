from rest_framework import serializers
from django.contrib.auth.models import User
from core.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя с полным набором полей"""
    class Meta:
        model = Users
        fields = '__all__'

class UsersLimitedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя с ограниченным набором полей"""
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'position']