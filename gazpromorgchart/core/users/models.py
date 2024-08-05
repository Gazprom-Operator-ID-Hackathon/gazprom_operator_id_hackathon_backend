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

    class Meta:
        verbose_name = 'IT компонент'
        verbose_name_plural = 'IT компоненты'

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

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name

class Position(models.Model):
    """Класс для модели должности"""
    name = models.CharField("Должность пользователя", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name

class Grade(models.Model):
    """Класс для модели грейда"""
    GRADE_CHOICES = [
        (1, 'Руководитель проектов'),
        (2, 'Руководитель департамента'),
        (3, 'Руководитель группы'),
        (4, 'Работник'),
    ]
    id = models.PositiveSmallIntegerField(choices=GRADE_CHOICES, primary_key=True)
    name = models.CharField("Грейд", max_length=50, blank=True, null=True)
    level = models.PositiveSmallIntegerField("Уровень иерархии", unique=True)

    class Meta:
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.get_id_display()

class EmployeeGrade(models.Model):
    """Класс для модели грейда сотрудника"""
    GRADE_CHOICES = [
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    ]
    id = models.PositiveSmallIntegerField(choices=GRADE_CHOICES, primary_key=True)
    name = models.CharField("Грейд сотрудника", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Грейд сотрудника'
        verbose_name_plural = 'Грейды сотрудников'

    def __str__(self):
        return self.get_id_display()

class EmploymentType(models.Model):
    """Класс для модели типа занятости"""
    name = models.CharField("Тип занятости", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'

    def __str__(self):
        return self.name

class ForeignLanguage(models.Model):
    """Класс для модели иностранных языков"""
    foreignlanguages = models.CharField(
        "Иностранные языки", max_length=255, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Иностранный язык'
        verbose_name_plural = 'Иностранные языки'

    def __str__(self):
        return self.foreignlanguages

class ProgrammingLanguages(models.Model):
    """Класс для модели языков программирования"""
    programminglanguages = models.CharField(
        "Языки программирования", max_length=255, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.programminglanguages

class ProgrammingSkills(models.Model):  
    """Класс для модели навыков программирования"""
    programmingskills = models.CharField(
        "Навыки программирования", max_length=255, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Навык программирования'
        verbose_name_plural = 'Навыки программирования'

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

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class User(models.Model):
    """Модель пользователя"""
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    photo = models.ImageField(
        "Фото пользователя", upload_to='user_photos/', blank=True, null=True
    )
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Должность')
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Грейд в структуре компании')
    employee_grade = models.ForeignKey(EmployeeGrade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Грейд сотрудника')
    boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates', verbose_name='Прямой руководитель')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members', verbose_name='Команда')
    it_component = models.ForeignKey(ITComponent, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип занятости')
    timezone = models.CharField(
        "Часовой пояс пользователя", max_length=32, choices=TIMEZONE_CHOICES, default='UTC'
    )
    foreign_languages = models.ManyToManyField(ForeignLanguage, blank=True, verbose_name='Иностранные языки')
    programming_languages = models.ManyToManyField(ProgrammingLanguages, blank=True, verbose_name='Языки программирования')
    programming_skills = models.ManyToManyField(ProgrammingSkills, blank=True, verbose_name='Навыки программирования')
    contacts = models.ManyToManyField(Contact, related_name='contacts', blank=True, verbose_name='Контакты')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"