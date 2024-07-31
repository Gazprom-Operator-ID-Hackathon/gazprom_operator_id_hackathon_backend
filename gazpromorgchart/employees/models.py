import pytz
from django.db import models

from .validators import (
    validate_links,
    validate_phone_numbers,
    validate_emails,
    validate_hashtags
)

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]


class EmploymentType(models.Model):
    """Модель видов занятости"""
    name = models.CharField(
        "Тип занятости",
        max_length=100,
        help_text="Тип занятости сотрудника"
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    """Модель должностей сотрудников"""
    title = models.CharField(
        max_length=100,
        verbose_name="Должность сотрудника",
    )

    def __str__(self):
        return self.title


class Grade(models.Model):
    """Модель грейда сотрудников"""
    name = models.CharField(
        "Грейд",
        max_length=50
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель сотрудника"""
    first_name = models.CharField(
        "Имя",
        max_length=100
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=100
    )
    photo = models.ImageField(
        "Фото сотрудника",
        upload_to='photos/',
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,  # Исправлено
        verbose_name="Позиция"
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,  # Исправлено
        verbose_name="Грейд"
    )
    employment_type = models.ForeignKey(
        EmploymentType,
        on_delete=models.SET_NULL,
        null=True,  # Исправлено
        verbose_name="Тип сотрудника"
    )
    timezone = models.CharField(
        "Часовой пояс сотрудника",
        max_length=32,
        choices=TIMEZONE_CHOICES,
        default='UTC',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    """Модель навыков сотрудника"""
    employee = models.ForeignKey(
        Employee,
        related_name='skills', 
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )
    foreign_languages = models.JSONField(
        "Иностранные языки",
        blank=True,
        null=True,
        validators=[validate_hashtags]
    )
    programs = models.JSONField(
        "Программы",
        blank=False,
        null=False,
        validators=[validate_hashtags]
    )
    skills = models.JSONField(
        "Навыки",
        blank=False,
        null=False,
        validators=[validate_hashtags]
    )

    def __str__(self):
        return f"Навыки {self.employee.first_name} {self.employee.last_name}"


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        "Наименование продукта",
        max_length=200
    )
    employee = models.ForeignKey(
        Employee,
        related_name='active_products',
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель проекта"""
    name = models.CharField(
        "Наименование проекта",
        max_length=200
    )
    employee = models.ForeignKey(
        Employee,
        related_name='completed_projects',
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Модель контактов сотрудника"""
    employee = models.ForeignKey(
        Employee,
        related_name='contacts',
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )
    email = models.JSONField(
        "Email", 
        blank=True,
        null=True,
        validators=[validate_emails]
    )
    phone = models.JSONField(
        "Телефон",
        blank=True,
        null=True,
        validators=[validate_phone_numbers]
    )
    links = models.JSONField(
        "Ссылки",
        blank=True,
        null=True,
        validators=[validate_links]
    )

    def __str__(self):
        return f"Contact of {self.employee.first_name} {self.employee.last_name}"


class Email(models.Model):
    """Модель для хранения нескольких адресов электронной почты"""
    contact = models.ForeignKey(
        Contact,
        related_name='emails',
        on_delete=models.CASCADE
    )
    email = models.EmailField("Email")

    def __str__(self):
        return self.email


class Phone(models.Model):
    """Модель для хранения нескольких телефонов"""
    contact = models.ForeignKey(Contact, related_name='phones', on_delete=models.CASCADE)
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.phone
