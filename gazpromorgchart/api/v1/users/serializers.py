from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from core.users.models import User, ITComponent, Team, Position, Grade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact
from django.contrib.auth import authenticate

class UserListSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'position']

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


class UserDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    grade = serializers.StringRelatedField()
    employment_type = serializers.StringRelatedField()
    foreign_languages = serializers.StringRelatedField(many=True)
    programming_languages = serializers.StringRelatedField(many=True)
    programming_skills = serializers.StringRelatedField(many=True)
    contacts = ContactSerializer(many=True, read_only=True)
    it_component = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = '__all__'