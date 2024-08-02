from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from core.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    class Meta:
        model = User
        fields = '__all__'

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
        
class RegisterSerializer(serializers.ModelSerializer):
    """Cериализатор для регистрации нового пользователя"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """Сериализатор для аутентификации пользователя"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)