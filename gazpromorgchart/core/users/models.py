from django.db import models
from django.contrib.auth import get_user_model
import pytz
from django.core.validators import MinValueValidator, MaxValueValidator

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

current_it_component_id = 100
current_team_id = 300
current_department_id = 200
current_user_id = 400


def generate_it_component_id():
    """Генерация ID для IT компонента"""
    global current_it_component_id
    current_it_component_id += 1
    return current_it_component_id


def generate_team_id():
    """Генерация ID для команды"""
    global current_team_id
    current_team_id += 1
    return current_team_id


def generate_department_id():
    """Генерация ID для департамента"""
    global current_department_id
    current_department_id += 1
    return current_department_id


def generate_user_id():
    """Генерация ID для пользователя"""
    global current_user_id
    current_user_id += 1
    return current_user_id


class ITComponent(models.Model):
    """
    Модель IT компонента.
    Содержит информацию о типе, статусе, командах и ресурсах компонента.
    """
    TYPE_CHOICES = [
        ('mobile', 'Мобильный'),
        ('web', 'Веб'),
        ('back', 'Бэкэнд'),
    ]
    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('inactive', 'Неактивный'),
    ]
    id = models.IntegerField(
        primary_key=True,
        default=generate_it_component_id
    )
    name = models.CharField(
        "Название компонента",
        max_length=100
    )
    description = models.TextField(
        "Описание компонента",
        blank=True,
        null=True
    )
    isActive = models.BooleanField(
        "Активен",
        default=True
    )
    teams = models.ManyToManyField(
        'Team',
        related_name='it_components',
        blank=True
    )
    component_leadId = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='component_lead'
    )
    type = models.CharField(
        "Тип",
        max_length=10,
        choices=TYPE_CHOICES,
        default='web'
    )
    status = models.CharField(
        "Статус",
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )
    resources = models.ManyToManyField(
        'Resources',
        related_name='it_components',
        blank=True
    )

    class Meta:
        verbose_name = "IT компонент"
        verbose_name_plural = "IT компоненты"

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    Модель команды.
    Содержит информацию о типе команды, руководителе,
    компонентах и пользователях.
    """
    TEAM_TYPE_CHOICES = [
        ('STAFF', 'Штатные'),
        ('OUTSOURCE', 'Аутсорс'),
    ]
    id = models.IntegerField(
        primary_key=True,
        default=generate_team_id
    )
    name = models.CharField(
        "Название команды",
        max_length=100
    )
    team_type = models.CharField(
        "Тип команды",
        max_length=10,
        choices=TEAM_TYPE_CHOICES
    )
    team_leadId = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lead_teams',
        verbose_name='Руководитель команды'
    )
    componentIds = models.ForeignKey(
        ITComponent,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='teams_in_team'
    )
    usersId = models.ManyToManyField(
        'User',
        related_name='teams_users',
        blank=True,
        verbose_name='Пользователи'
    )
    departmentId = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teams_department',
        verbose_name='Департамент'
    )
    performance = models.TextField(
        "Эффективность",
        blank=True,
        null=True
    )
    description = models.TextField(
        "Описание",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return self.name


class Position(models.Model):
    """Класс для модели должности в компании"""
    name = models.CharField(
        "Должность пользователя",
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name or ""


class Grade(models.Model):
    """Класс для модели грейда"""
    GRADE_CHOICES = [
        (1, 'Руководитель проектов'),
        (2, 'Руководитель департамента'),
        (3, 'Руководитель группы'),
        (4, 'Работник'),
    ]
    id = models.PositiveSmallIntegerField(
        choices=GRADE_CHOICES,
        primary_key=True
    )

    class Meta:
        verbose_name = "Грейд"
        verbose_name_plural = "Грейды"

    def __str__(self):
        return dict(self.GRADE_CHOICES).get(self.id, "")


class EmployeeGrade(models.Model):
    """Класс для модели грейда сотрудника"""
    GRADE_CHOICES = [
        ('Junior', 'Junior'),
        ('Junior+', 'Junior+'),
        ('Middle', 'Middle'),
        ('Middle+', 'Middle+'),
        ('Senior', 'Senior'),
        ('Team Lead', 'Team Lead'),
    ]
    id = models.CharField(
        max_length=10,
        choices=GRADE_CHOICES,
        primary_key=True
    )

    class Meta:
        verbose_name = "Грейд сотрудника"
        verbose_name_plural = "Грейды сотрудников"

    def __str__(self):
        return str(self.id)


class EmploymentType(models.Model):
    """Класс для модели типа занятости"""
    EMPLOYMENT_TYPE_CHOICES = [
        ('FULL_TIME', 'Полная занятость'),
        ('PART_TIME', 'Частичная занятость'),
        ('CONTRACT', 'Контракт'),
        ('TEMPORARY', 'Временная занятость'),
        ('INTERN', 'Стажировка'),
        ('FREELANCE', 'Фриланс'),
    ]
    employment_type = models.CharField(
        "Тип занятости",
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES
    )

    class Meta:
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'

    def __str__(self):
        return self.employment_type


class ForeignLanguage(models.Model):
    """Класс для модели иностранных языков"""
    foreignlanguages = models.CharField(
        "Иностранные языки",
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Иностранный язык'
        verbose_name_plural = 'Иностранные языки'

    def __str__(self):
        return self.foreignlanguages


class ProgrammingLanguages(models.Model):
    """Класс для модели языков программирования"""
    programminglanguages = models.CharField(
        "Языки программирования",
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.programminglanguages


class ProgrammingSkills(models.Model):
    """Класс для модели навыков программирования"""
    programmingskills = models.CharField(
        "Навыки программирования",
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Навык программирования'
        verbose_name_plural = 'Навыки программирования'

    def __str__(self):
        return self.programmingskills


class Contact(models.Model):
    """Класс для модели контактов"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    links = models.JSONField(
        "Ссылки",
        default=list,
        blank=True
    )
    emails = models.JSONField(
        "Электронные почты",
        default=list,
        blank=True
    )
    phones = models.JSONField(
        "Телефоны",
        default=list,
        blank=True
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        if isinstance(self.emails, list):
            return ', '.join(self.emails)
        return str(self.emails)


class User(models.Model):
    """Модель пользователя"""
    id = models.IntegerField(
        primary_key=True,
        default=generate_user_id
    )
    first_name = models.CharField(
        "Имя",
        max_length=100
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=100
    )
    photo = models.ImageField(
        "Фото пользователя",
        upload_to='user_photos/',
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Должность'
    )
    level = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Грейд в структуре компании'
    )
    grade = models.ForeignKey(
        EmployeeGrade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Грейд сотрудника'
    )
    bossId = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name='Прямой руководитель'
    )
    teamId = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members',
        verbose_name='Команда'
    )
    componentId = models.ForeignKey(
        ITComponent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    employment_type = models.ForeignKey(
        EmploymentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тип занятости'
    )
    timezone = models.CharField(
        "Часовой пояс пользователя",
        max_length=32,
        choices=TIMEZONE_CHOICES,
        default='UTC'
    )
    town = models.CharField(
        "Город",
        max_length=100,
        default='Москва'
    )
    foreign_languages = models.ManyToManyField(
        ForeignLanguage,
        blank=True,
        verbose_name='Иностранные языки'
    )
    programs = models.ManyToManyField(
        ProgrammingLanguages,
        blank=True,
        verbose_name='Языки программирования'
    )
    skills = models.ManyToManyField(
        ProgrammingSkills,
        blank=True,
        verbose_name='Навыки программирования'
    )
    contacts = models.ManyToManyField(
        Contact,
        blank=True,
        verbose_name='Контакты',
        related_name='user_contacts'
    )
    departmentId = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name='Департамент'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Department(models.Model):
    """
    Модель департамента.
    Содержит информацию о департаменте, его названии, руководителе и командах.
    """
    DEPARTMENT_NAME_CHOICES = [
        ('Дизайн', 'Дизайн'),
        ('Девелопмент', 'Девелопмент'),
        ('Анализ', 'Анализ'),
        ('Менеджмент', 'Менеджмент'),
        ('Маркетинг', 'Маркетинг'),
        ('HR', 'HR'),
        ('Девопсы', 'Девопсы'),
    ]
    id = models.IntegerField(
        primary_key=True,
        default=generate_department_id
    )
    name = models.CharField(
        max_length=100,
        choices=DEPARTMENT_NAME_CHOICES
    )
    department_leadId = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='lead_departments'
    )
    teamsId = models.ManyToManyField(
        Team,
        related_name='departments',
        blank=True,
        verbose_name='ID групп'
    )

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return self.name


class Resources(models.Model):
    """
    Модель ресурсов.
    Содержит информацию о ресурсах команды, их стоимости и прогрессе.
    """
    teamId = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE
    )
    cost = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100000)]
    )
    progress = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"{self.teamId.name} - {self.cost} - {self.progress}%"
