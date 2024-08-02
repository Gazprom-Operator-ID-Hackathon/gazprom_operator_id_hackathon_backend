import os
import django
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from core.users.models import Users, TIMEZONE_CHOICES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gazpromorgchart.settings')
django.setup()

fake = Faker('ru_RU')  # Используем русскую локализацию

IT_POSITIONS = [
    'Программист',
    'Системный администратор',
    'Аналитик данных',
    'Разработчик ПО',
    'Тестировщик',
    'Менеджер проектов',
    'Сетевой инженер',
    'Специалист по информационной безопасности',
    'Веб-разработчик',
    'Инженер DevOps'
]

class Command(BaseCommand):
    help = 'Создание тестовых пользователей'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество тестовых пользователей для создания')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            self.create_test_user()

    def create_test_user(self):
        username = fake.user_name()
        email = fake.email()
        password = 'password123'
        first_name = fake.first_name()
        last_name = fake.last_name()

        # Создание пользователя
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        user_profile = Users.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            photo=None,
            position=fake.random_element(elements=IT_POSITIONS),  # Используем IT должности
            grade=fake.random_element(elements=('A', 'B', 'C', 'D')),
            employment_type=fake.random_element(elements=('Full-time', 'Part-time', 'Contract')),
            timezone=fake.random_element(elements=[tz for tz, _ in TIMEZONE_CHOICES]),
            foreign_languages=fake.words(nb=3),
            programs=fake.words(nb=3),
            skills=fake.words(nb=3),
            products=fake.words(nb=3),
            projects=fake.words(nb=3),
            contacts={
                'email': fake.email(),
                'phone': fake.phone_number(),
                'link': fake.url()
            }
        )
        user_profile.save()

        self.stdout.write(self.style.SUCCESS(f'Пользователь {username} создан'))

if __name__ == '__main__':
    Command().handle(total=10)