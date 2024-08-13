from django.contrib import admin
from .models import (
    ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, 
    ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, 
    Contact, User, Department, Resources
)

@admin.register(ITComponent)
class ITComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'isActive', 'type', 'status')
    search_fields = ('name', 'type', 'status')
    filter_horizontal = ('teams', 'resources')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_type', 'team_leadId', 'componentIds', 'departmentId')
    search_fields = ('name', 'team_type')
    filter_horizontal = ('usersId',)

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
    list_display = ('user',)
    search_fields = ('user',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_leadId')
    search_fields = ('name',)
    filter_horizontal = ('teamsId',)