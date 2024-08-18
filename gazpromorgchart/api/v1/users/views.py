from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from core.users.models import (
    User, Department, Resources, ITComponent, Team, Position, Grade,
    EmployeeGrade, EmploymentType, ForeignLanguage, ProgrammingLanguages,
    ProgrammingSkills
)
from .serializers import (
    DepartmentSerializer, UserListSerializer, UserDetailSerializer,
    ITComponentSerializer, TeamSerializer, PositionSerializer,
    GradeSerializer, EmployeeGradeSerializer, EmploymentTypeSerializer,
    ForeignLanguageSerializer, ProgrammingLanguagesSerializer,
    ProgrammingSkillsSerializer, ContactSerializer, ResourcesSerializer
)


class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели User."""
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserMeView(APIView):
    """Вьюсет для получения информации о текущем пользователе."""

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения, обновления и удаления пользователя."""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'


class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели ITComponent."""
    queryset = ITComponent.objects.all()
    serializer_class = ITComponentSerializer


class ITComponentViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели ITComponent."""
    queryset = ITComponent.objects.all()
    serializer_class = ITComponentSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Team."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Position."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class GradeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Grade."""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class EmployeeGradeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели EmployeeGrade."""
    queryset = EmployeeGrade.objects.all()
    serializer_class = EmployeeGradeSerializer


class EmploymentTypeViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели EmploymentType."""
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer


class ForeignLanguageViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели ForeignLanguage."""
    queryset = ForeignLanguage.objects.all()
    serializer_class = ForeignLanguageSerializer


class ProgrammingLanguagesViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели ProgrammingLanguages."""
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class ProgrammingSkillsViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели ProgrammingSkills."""
    queryset = ProgrammingSkills.objects.all()
    serializer_class = ProgrammingSkillsSerializer


class UserContactsView(generics.ListAPIView):
    """Вьюсет для получения контактов пользователя по его ID."""
    serializer_class = ContactSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Department."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ProjectsView(APIView):
    """Вьюсет для получения всех проектов, департаментов и команд."""
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


class ResourcesViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Resources."""
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
