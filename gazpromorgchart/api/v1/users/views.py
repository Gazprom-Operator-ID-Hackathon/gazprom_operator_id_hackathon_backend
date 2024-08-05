from rest_framework import viewsets, generics, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.shortcuts import redirect
from core.users.models import (
    User, ITComponent, Team, Position, Grade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact
)
from .serializers import (
    UserSerializer, UserListSerializer, UserDetailSerializer, ITComponentSerializer, TeamSerializer, PositionSerializer, 
    GradeSerializer, EmploymentTypeSerializer, ForeignLanguageSerializer, ProgrammingLanguagesSerializer, ProgrammingSkillsSerializer, ContactSerializer
)

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для получения списка пользователей с ограниченным набором полей"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    operation_description = "Получение списка пользователей для формирования диаграммы"

class UserMeView(APIView):
    """Вьюсет для перенаправления на профиль первого пользователя"""
    def get(self, request, *args, **kwargs):
        return redirect('user-detail', pk=1)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения данных другого пользователя по ID и выполнения CRUD операций"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'
    operation_description = "Получение, создание, обновление и удаление данных пользователя по ID"

class ITComponentViewSet(viewsets.ModelViewSet):
    queryset = ITComponent.objects.all()
    serializer_class = ITComponentSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class EmploymentTypeViewSet(viewsets.ModelViewSet):
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer

class ForeignLanguageViewSet(viewsets.ModelViewSet):
    queryset = ForeignLanguage.objects.all()
    serializer_class = ForeignLanguageSerializer

class ProgrammingLanguagesViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer

class ProgrammingSkillsViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingSkills.objects.all()
    serializer_class = ProgrammingSkillsSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer