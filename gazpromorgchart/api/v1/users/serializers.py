from rest_framework import serializers
from core.users.models import (
    User, Department, ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact
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
        fields = ['name', 'id', 'it_component', 'employees']

class ITComponentSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = ITComponent
        fields = ['name', 'id', 'teams']

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
        fields = ['links', 'emails', 'phones']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'links': representation['links'],
            'emails': representation['emails'],
            'phones': representation['phones']
        }

class UserDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    contacts = serializers.SerializerMethodField()
    foreign_languages = serializers.StringRelatedField(many=True)
    programs = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)
    employment_type = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'photo', 'position', 'level', 'grade', 
            'bossId', 'teamId', 'componentId', 'employment_type', 'timezone', 'town', 
            'foreign_languages', 'programs', 'skills', 'contacts'
        ]

    def get_contacts(self, obj):
        contact = Contact.objects.filter(user=obj).first()
        return ContactSerializer(contact).data if contact else None

class DepartmentSerializer(serializers.ModelSerializer):
    department_leadId = serializers.PrimaryKeyRelatedField(source='department_lead', queryset=User.objects.all())
    teamId = serializers.PrimaryKeyRelatedField(source='teams', many=True, queryset=Team.objects.all())

    class Meta:
        model = Department
        fields = ['name', 'id', 'department_leadId', 'teamId']