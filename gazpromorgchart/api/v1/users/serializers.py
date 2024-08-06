from rest_framework import serializers
from core.users.models import (
    User, ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact
)

class UserListSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'position']

class UserDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    contacts = serializers.SerializerMethodField()
    foreign_languages = serializers.StringRelatedField(many=True)
    programming_languages = serializers.StringRelatedField(many=True)
    programming_skills = serializers.StringRelatedField(many=True)
    employment_type = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'photo', 'position', 'level', 'grade', 'bossId', 'teamId', 'componentId',
            'employment_type', 'timezone', 'town', 'foreign_languages', 'programming_languages', 'programming_skills', 'contacts'
        ]

    def get_contacts(self, obj):
        contacts = Contact.objects.filter(user=obj)
        return ContactSerializer(contacts, many=True).data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ITComponentSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField(many=True)

    class Meta:
        model = ITComponent
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_users(self, obj):
        users = obj.users.all()
        return UserListSerializer(users, many=True).data

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
    links = serializers.SerializerMethodField()
    emails = serializers.SerializerMethodField()
    phones = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['links', 'emails', 'phones']

    def get_links(self, obj):
        return [obj.social_link1, obj.social_link2, obj.social_link3]

    def get_emails(self, obj):
        return [obj.email1, obj.email2]

    def get_phones(self, obj):
        return [obj.phone1, obj.phone2]
