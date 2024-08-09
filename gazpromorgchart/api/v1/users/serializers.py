from rest_framework import serializers
from core.users.models import (
    User, Department, ITComponent, Team, Position, Grade, EmployeeGrade,
    EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills,
    Contact, Resources
)

class UserListSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'position']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'id', 'team_leadId', 'componentIds', 'usersId', 'departmentId', 'performance', 'description', 'links')

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['teamId', 'cost', 'progress']

class ITComponentSerializer(serializers.ModelSerializer):
    resources = ResourcesSerializer(many=True, read_only=True)

    class Meta:
        model = ITComponent
        fields = ['name', 'id', 'component_leadId', 'resources', 'isActive', 'type']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class EmployeeGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGrade
        fields = '__all__'

class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentType
        fields = '__all__'

class ForeignLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignLanguage
        fields = '__all__'

class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = '__all__'

class ProgrammingSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingSkills
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)

class UserDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    contacts = serializers.SerializerMethodField()
    foreign_languages = serializers.StringRelatedField(many=True)
    programs = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)
    employment_type = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = '__all__'

    def get_contacts(self, obj):
        return ContactSerializer(obj.contacts.all(), many=True).data

class DepartmentSerializer(serializers.ModelSerializer):
    department_leadId = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    teamsId = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

    class Meta:
        model = Department
        fields = ['name', 'id', 'department_leadId', 'teamsId']

class CombinedSerializer(serializers.Serializer):
    components = ITComponentSerializer(many=True)
    departments = DepartmentSerializer(many=True)
    teams = TeamSerializer(many=True)