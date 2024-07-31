from rest_framework import serializers
from core.employees.models import (
    EmploymentType, Position, Grade, 
    Employee, Skill, Product, Project, 
    Contact, Email, Phone
)


class EmploymentTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели видов занятости"""
    class Meta:
        model = EmploymentType
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели должностей сотрудников"""
    class Meta:
        model = Position
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели грейда сотрудников"""
    class Meta:
        model = Grade
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сотрудника"""
    class Meta:
        model = Employee
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор для модели навыков сотрудника"""
    class Meta:
        model = Skill
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукта"""
    class Meta:
        model = Product
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор для модели проекта"""
    class Meta:
        model = Project
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для модели контактов сотрудника"""
    class Meta:
        model = Contact
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели адресов электронной почты"""
    class Meta:
        model = Email
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    """Сериализатор для модели телефонов"""
    class Meta:
        model = Phone
        fields = '__all__'