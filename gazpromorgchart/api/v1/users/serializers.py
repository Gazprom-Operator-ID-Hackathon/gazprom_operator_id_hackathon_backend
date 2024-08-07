from rest_framework import serializers
from core.users.models import (
    User, ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact
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