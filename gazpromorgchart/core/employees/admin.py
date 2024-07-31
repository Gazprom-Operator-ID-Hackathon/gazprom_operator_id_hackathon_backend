from django.contrib import admin
from .models import (
    EmploymentType, Position, Grade, Employee, Skill, 
    Product, Project, Contact, Email, Phone
)

admin.site.register(EmploymentType)
admin.site.register(Position)
admin.site.register(Grade)
admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(Phone)