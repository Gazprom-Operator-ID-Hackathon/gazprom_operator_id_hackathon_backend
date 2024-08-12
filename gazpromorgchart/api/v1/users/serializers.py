from rest_framework import serializers
from core.users.models import (
    User, Department, ITComponent, Team, Position, Grade, EmployeeGrade,
    EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills,
    Contact, Resources
)

class UserContactLinksSerializer(serializers.Serializer):
    links = serializers.ListField(child=serializers.URLField())
    emails = serializers.ListField(child=serializers.EmailField())
    phones = serializers.ListField(child=serializers.CharField())



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'

class ITComponentSerializer(serializers.ModelSerializer):
    resources = ResourcesSerializer(many=True, read_only=True)

    class Meta:
        model = ITComponent
        fields = '__all__'

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

class UserListSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='position.name', read_only=True)
    level = serializers.CharField(source='grade.id', read_only=True)
    bossId = serializers.IntegerField(source='bossId.id', read_only=True)
    componentId = serializers.IntegerField(source='componentId.id', read_only=True)
    teamId = serializers.IntegerField(source='teamId.id', read_only=True)
    departmentId = serializers.IntegerField(source='departmentId.id', read_only=True)
    employment_type = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'photo', 'position', 'level', 
            'bossId', 'componentId', 'teamId', 'departmentId', 'employment_type', 
            'town', 'timezone', 'contacts'
        ]

    def get_employment_type(self, obj):
        if obj.employment_type:
            return dict(EmploymentType.EMPLOYMENT_TYPE_CHOICES).get(obj.employment_type.employment_type)
        return None

    def get_contacts(self, obj):
        links = []
        for contact in obj.contacts.all():
            links.extend(contact.links)
        return {'links': links}

class UserDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    grade = serializers.StringRelatedField()
    employment_type = serializers.SerializerMethodField()
    foreign_languages = serializers.StringRelatedField(many=True)
    programs = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'photo', 'position', 'level', 
            'grade', 'bossId', 'teamId', 'componentId', 'departmentId', 
            'employment_type', 'timezone', 'town', 'foreign_languages', 
            'programs', 'skills', 'contacts'
        ]

    def get_employment_type(self, obj):
        if obj.employment_type:
            return dict(EmploymentType.EMPLOYMENT_TYPE_CHOICES).get(obj.employment_type.employment_type)
        return None

    def get_contacts(self, obj):
        links = []
        emails = []
        phones = []
        for contact in obj.contacts.all():
            links.extend(contact.links)
            emails.extend(contact.emails)
            phones.extend(contact.phones)
        return {'links': links, 'emails': emails, 'phones': phones}

class DepartmentSerializer(serializers.ModelSerializer):
    department_leadId = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    teamsId = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

    class Meta:
        model = Department
        fields = '__all__'

class CombinedSerializer(serializers.Serializer):
    components = ITComponentSerializer(many=True)
    departments = DepartmentSerializer(many=True)
    teams = TeamSerializer(many=True)