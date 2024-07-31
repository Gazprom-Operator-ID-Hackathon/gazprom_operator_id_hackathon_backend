from rest_framework import viewsets
from core.employees.models import (
    EmploymentType, Position, Grade, Employee, Skill, 
    Product, Project, Contact, Email, Phone
)
from .serializers import (
    EmploymentTypeSerializer, PositionSerializer, GradeSerializer, 
    EmployeeSerializer, SkillSerializer, ProductSerializer, 
    ProjectSerializer, ContactSerializer, EmailSerializer, 
    PhoneSerializer
)


class EmploymentTypeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели видов занятости"""
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели должностей сотрудников"""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class GradeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели грейда сотрудников"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели навыков сотрудника"""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели проекта"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели контактов сотрудника"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class EmailViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели адресов электронной почты"""
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели телефонов"""
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
