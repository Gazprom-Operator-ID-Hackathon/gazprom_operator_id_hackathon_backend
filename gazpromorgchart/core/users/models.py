from django.db import models
from django.contrib.auth.models import User
import pytz

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

class ITComponent(models.Model):
    """Модель IT компонента"""
    STATUS_CHOICES = [
        ('ACTIVE', 'Активный'),
        ('COMPLETED', 'Завершенный'),
    ]
    name = models.CharField("Название компонента", max_length=100)
    description = models.TextField("Описание компонента", blank=True, null=True)
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.name

class Team(models.Model):
    """Модель команды"""
    TEAM_TYPE_CHOICES = [
        ('STAFF', 'Штатные'),
        ('OUTSOURCE', 'Аутсорс'),
        ('VIRTUAL', 'Виртуальные'),
    ]
    name = models.CharField("Название команды", max_length=100)
    team_type = models.CharField("Тип команды", max_length=10, choices=TEAM_TYPE_CHOICES)
    it_component = models.ForeignKey(ITComponent, on_delete=models.CASCADE, related_name='teams')
    employees = models.ManyToManyField(User, related_name='teams', blank=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    """Класс для модели должности"""
    name = models.CharField("Должность пользователя", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    """Класс для модели грейда"""
    name = models.CharField("Грейд", max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class EmploymentType(models.Model):
    """Класс для модели типа занятости"""
    name = models.CharField("Тип занятости", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class ForeignLanguage(models.Model):
    """Класс для модели иностранных языков"""
    foreignlanguages = models.CharField(
        "Иностранные языки", max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.foreignlanguages

class ProgrammingLanguages(models.Model):
    """Класс для модели языков программирования"""
    programminglanguages = models.CharField(
        "Языки программирования", max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.programminglanguages

class ProgrammingSkills(models.Model):  
    """Класс для модели навыков программирования"""
    programmingskills = models.CharField(
        "Навыки программирования", max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.programmingskills

class Contact(models.Model):
    """Класс для модели контактов"""
    user = models.ForeignKey(User, related_name='user_contacts', on_delete=models.CASCADE)
    email1 = models.EmailField("Электронная почта 1", blank=True, null=True)
    email2 = models.EmailField("Электронная почта 2", blank=True, null=True)
    phone1 = models.CharField("Телефон 1", max_length=50, blank=True, null=True)
    phone2 = models.CharField("Телефон 2", max_length=50, blank=True, null=True)
    social_link1 = models.URLField("Социальная ссылка 1", blank=True, null=True)
    social_link2 = models.URLField("Социальная ссылка 2", blank=True, null=True)
    social_link3 = models.URLField("Социальная ссылка 3", blank=True, null=True)

class User(models.Model):
    """Модель пользователя"""
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    photo = models.ImageField(
        "Фото пользователя", upload_to='user_photos/', blank=True, null=True
    )
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True, blank=True)
    timezone = models.CharField(
        "Часовой пояс пользователя", max_length=32, choices=TIMEZONE_CHOICES, default='UTC'
    )
    foreign_languages = models.ManyToManyField(ForeignLanguage, blank=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguages, blank=True)
    programming_skills = models.ManyToManyField(ProgrammingSkills, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='contacts', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"