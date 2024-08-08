from django.contrib import admin
from .models import (
    ITComponent, Team, Position, Grade, EmployeeGrade, EmploymentType, 
    ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, 
    Contact, User, Department
)

admin.site.register(ITComponent)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(Grade)
admin.site.register(EmployeeGrade)
admin.site.register(EmploymentType)
admin.site.register(ForeignLanguage)
admin.site.register(ProgrammingLanguages)
admin.site.register(ProgrammingSkills)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Department)