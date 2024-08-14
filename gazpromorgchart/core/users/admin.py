from django.contrib import admin
from .models import (
    ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType,
    ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact, User,
    Department, Resources
)


@admin.register(ITComponent)
class ITComponentAdmin(admin.ModelAdmin):
    """Админка для модели ITComponent."""
    list_display = ('name', 'isActive')
    search_fields = ('name',)
    filter_horizontal = ('teams',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Админка для модели Team."""
    list_display = ('name', 'team_type', 'componentIds')
    search_fields = ('name', 'team_type')
    filter_horizontal = ('usersId',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Админка для модели Position."""
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """Админка для модели Grade."""
    list_display = ('id',)
    search_fields = ('id',)


@admin.register(EmployeeGrade)
class EmployeeGradeAdmin(admin.ModelAdmin):
    """Админка для модели EmployeeGrade."""
    list_display = ('id',)
    search_fields = ('id',)


@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    """Админка для модели EmploymentType."""
    list_display = ('employment_type',)
    search_fields = ('employment_type',)


@admin.register(ForeignLanguage)
class ForeignLanguageAdmin(admin.ModelAdmin):
    """Админка для модели ForeignLanguage."""
    list_display = ('foreignlanguages',)
    search_fields = ('foreignlanguages',)


@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    """Админка для модели ProgrammingLanguages."""
    list_display = ('programminglanguages',)
    search_fields = ('programminglanguages',)


@admin.register(ProgrammingSkills)
class ProgrammingSkillsAdmin(admin.ModelAdmin):
    """Админка для модели ProgrammingSkills."""
    list_display = ('programmingskills',)
    search_fields = ('programmingskills',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админка для модели Contact."""
    list_display = ('user', 'emails')
    search_fields = ('user__first_name', 'user__last_name', 'emails')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для модели User."""
    list_display = (
        'first_name', 'last_name', 'position', 'level', 'grade',
        'employment_type', 'timezone', 'town'
    )
    search_fields = (
        'first_name', 'last_name', 'position__name', 'level__id',
        'grade__id', 'employment_type__employment_type', 'town'
    )
    filter_horizontal = ('foreign_languages', 'programs', 'skills', 'contacts')

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            super().save_model(request, obj, form, change)


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    """Админка для модели Resources."""
    list_display = ('teamId', 'cost', 'progress')
    search_fields = ('teamId__name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Админка для модели Department."""
    list_display = ('name', 'department_leadId')
    search_fields = (
        'name', 'department_leadId__first_name', 'department_leadId__last_name'
    )
    filter_horizontal = ('teamsId',)
