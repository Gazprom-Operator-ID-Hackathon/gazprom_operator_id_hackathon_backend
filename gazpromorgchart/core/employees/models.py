import pytz
from django.db import models

from .validators import (
    validate_links,
    validate_phone_numbers,
    validate_emails,
    validate_hashtags
)

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]


class Employee(models.Model):
    """Модель сотрудника"""
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    photo = models.ImageField(
        "Фото сотрудника", upload_to='photos/', blank=True, null=True
    )
    position = models.CharField("Должность сотрудника", max_length=100)
    grade = models.CharField("Грейд", max_length=50)
    employment_type = models.CharField("Тип занятости", max_length=100)
    timezone = models.CharField(
        "Часовой пояс сотрудника", max_length=32, choices=TIMEZONE_CHOICES, 
        default='UTC'
    )
    foreign_languages = models.JSONField(
        "Иностранные языки", blank=True, null=True, validators=[validate_hashtags]
    )
    programs = models.JSONField(
        "Программы", blank=False, null=False, validators=[validate_hashtags]
    )
    skills = models.JSONField(
        "Навыки", blank=False, null=False, validators=[validate_hashtags]
    )
    products = models.JSONField("Продукты", blank=True, null=True)
    projects = models.JSONField("Проекты", blank=True, null=True)
    contacts = models.JSONField(
        "Контакты", blank=True, null=True, 
        validators=[validate_emails, validate_phone_numbers, validate_links]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"