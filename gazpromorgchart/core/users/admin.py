from django.contrib import admin
from .models import (
    ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, 
    ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, 
    Contact, User, Department
)

@admin.register(ITComponent)
class ITComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'status')
    filter_horizontal = ('teams',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_type', 'it_component')
    search_fields = ('name', 'team_type')
    filter_horizontal = ('employees',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(EmployeeGrade)
class EmployeeGradeAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ('employment_type',)
    search_fields = ('employment_type',)

@admin.register(ForeignLanguage)
class ForeignLanguageAdmin(admin.ModelAdmin):
    list_display = ('foreignlanguages',)
    search_fields = ('foreignlanguages',)

@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    list_display = ('programminglanguages',)
    search_fields = ('programminglanguages',)

@admin.register(ProgrammingSkills)
class ProgrammingSkillsAdmin(admin.ModelAdmin):
    list_display = ('programmingskills',)
    search_fields = ('programmingskills',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'emails')
    search_fields = ('user__first_name', 'user__last_name', 'emails')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'level', 'grade', 'employment_type', 'timezone', 'town')
    search_fields = ('first_name', 'last_name', 'position__name', 'level__id', 'grade__id', 'employment_type__employment_type', 'town')
    filter_horizontal = ('foreign_languages', 'programs', 'skills', 'contacts')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_leadId')
    search_fields = ('name', 'department_lead__first_name', 'department_lead__last_name')
    filter_horizontal = ('teams',)