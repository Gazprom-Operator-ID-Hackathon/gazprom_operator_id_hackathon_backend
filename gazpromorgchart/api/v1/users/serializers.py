from rest_framework import serializers

from core.users.models import (
    User, Department, ITComponent, Team, Position, Grade, EmployeeGrade,
    EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills,
    Contact, Resources
)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Team."""
    class Meta:
        model = Team
        fields = '__all__'


class ResourcesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Resources."""
    class Meta:
        model = Resources
        fields = '__all__'


class ITComponentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ITComponent."""
    resources = ResourcesSerializer(many=True, read_only=True)

    class Meta:
        model = ITComponent
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Position."""
    class Meta:
        model = Position
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Grade."""
    class Meta:
        model = Grade
        fields = '__all__'


class EmployeeGradeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели EmployeeGrade."""
    class Meta:
        model = EmployeeGrade
        fields = '__all__'


class EmploymentTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели EmploymentType."""
    class Meta:
        model = EmploymentType
        fields = '__all__'


class ForeignLanguageSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ForeignLanguage."""
    class Meta:
        model = ForeignLanguage
        fields = '__all__'


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ProgrammingLanguages."""
    class Meta:
        model = ProgrammingLanguages
        fields = '__all__'


class ProgrammingSkillsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ProgrammingSkills."""
    class Meta:
        model = ProgrammingSkills
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Contact."""
    class Meta:
        model = Contact
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка пользователей."""
    position = serializers.CharField(source='position.name', read_only=True)
    grade = serializers.StringRelatedField()
    bossId = serializers.IntegerField(source='bossId.id', read_only=True)
    componentId = serializers.IntegerField(
        source='componentId.id', read_only=True
    )
    teamId = serializers.IntegerField(source='teamId.id', read_only=True)
    departmentId = serializers.IntegerField(
        source='departmentId.id', read_only=True
    )
    employment_type = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'photo', 'position', 'level', 'grade',
            'bossId', 'componentId', 'teamId', 'departmentId', 
            'employment_type', 'town', 'timezone', 'contacts'
        ]

    def get_employment_type(self, obj):
        if obj.employment_type:
            return dict(
                EmploymentType.EMPLOYMENT_TYPE_CHOICES
            ).get(obj.employment_type.employment_type)
        return None

    def get_contacts(self, obj):
        links = []
        for contact in obj.contacts.all():
            links.extend(contact.links)
        return {'links': links}


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о пользователе."""
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
            return dict(
                EmploymentType.EMPLOYMENT_TYPE_CHOICES
            ).get(obj.employment_type.employment_type)
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
    """Сериализатор для модели Department."""
    department_leadId = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    teamsId = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Team.objects.all()
    )

    class Meta:
        model = Department
        fields = '__all__'
