from django.contrib import admin
from .models import (
    ITComponent, Team, Position, Grade, EmploymentType, 
    ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, 
    Contact, User
)

admin.site.register(ITComponent)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(Grade)
admin.site.register(EmploymentType)
admin.site.register(ForeignLanguage)
admin.site.register(ProgrammingLanguages)
admin.site.register(ProgrammingSkills)
admin.site.register(Contact)
admin.site.register(User)