from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from core.users.models import (
    User, Department, Contact, ITComponent, Team, Position, Grade, 
    EmployeeGrade, EmploymentType, ForeignLanguage, ProgrammingLanguages, 
    ProgrammingSkills
)
from .serializers import (
    DepartmentSerializer, UserListSerializer, UserDetailSerializer, 
    ITComponentSerializer, TeamSerializer, PositionSerializer, 
    GradeSerializer, EmployeeGradeSerializer, EmploymentTypeSerializer, 
    ForeignLanguageSerializer, ProgrammingLanguagesSerializer, 
    ProgrammingSkillsSerializer, ContactSerializer, UserSerializer,
    MyTokenObtainPairSerializer
)

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'

class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ITComponent.objects.all()
    serializer_class = ITComponentSerializer

class ITComponentViewSet(viewsets.ReadOnlyModelViewSet):
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

class EmployeeGradeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeGrade.objects.all()
    serializer_class = EmployeeGradeSerializer

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

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        components = ITComponent.objects.all()
        departments = Department.objects.all()
        teams = Team.objects.all()

        components_serializer = ITComponentSerializer(components, many=True)
        departments_serializer = DepartmentSerializer(departments, many=True)
        teams_serializer = TeamSerializer(teams, many=True)

        combined_data = {
            'components': components_serializer.data,
            'departments': departments_serializer.data,
            'teams': teams_serializer.data
        }

        return Response(combined_data)

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer