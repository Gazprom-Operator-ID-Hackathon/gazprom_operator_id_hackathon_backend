import random
from django.core.management.base import BaseCommand
from faker import Faker
from core.users.models import User, Position, Grade, EmploymentType, ForeignLanguage, ProgrammingLanguages, ProgrammingSkills, Contact

fake = Faker()

class Command(BaseCommand):
    help = 'Создание тестовых пользователей'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        positions = Position.objects.all()
        grades = Grade.objects.all()
        employment_types = EmploymentType.objects.all()
        foreign_languages = ForeignLanguage.objects.all()
        programming_languages = ProgrammingLanguages.objects.all()
        programming_skills = ProgrammingSkills.objects.all()

        for _ in range(n):
            user = User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                position=random.choice(positions) if positions else None,
                grade=random.choice(grades) if grades else None,
                employment_type=random.choice(employment_types) if employment_types else None,
            )
            if foreign_languages:
                user.foreign_languages.set([random.choice(foreign_languages)])
            if programming_languages:
                user.programming_languages.set([random.choice(programming_languages)])
            if programming_skills:
                user.programming_skills.set([random.choice(programming_skills)])
            
            Contact.objects.create(
                user=user,
                email1=fake.email(),
                phone1=fake.phone_number(),
                social_link1=fake.url(),
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {n} users'))