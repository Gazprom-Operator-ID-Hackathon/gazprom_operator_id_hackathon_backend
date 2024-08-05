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
    User, Contact, ITComponent, Team, Position, Grade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills
)
from .serializers import (
    UserSerializer, UserListSerializer, UserDetailSerializer, ITComponentSerializer, TeamSerializer, PositionSerializer, 
    GradeSerializer, EmploymentTypeSerializer, ForeignLanguageSerializer, ProgrammingLanguagesSerializer, ProgrammingSkillsSerializer, ContactSerializer
)

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для получения списка пользователей с ограниченным набором полей"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserMeView(APIView):
    """Вьюсет для получения данных текущего пользователя"""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения данных другого пользователя по ID и выполнения CRUD операций"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'

class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для получения списка проектов"""
    queryset = ITComponent.objects.all()
    serializer_class = ITComponentSerializer

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

class UserContactsView(generics.ListAPIView):
    """Вьюсет для получения контактов пользователя по его ID"""
    serializer_class = ContactSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Contact.objects.none()
        user_id = self.kwargs['pk']
        return Contact.objects.filter(user=user_id)