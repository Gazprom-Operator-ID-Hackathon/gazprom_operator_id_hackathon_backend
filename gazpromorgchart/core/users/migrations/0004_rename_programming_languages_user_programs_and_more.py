# Generated by Django 4.2.4 on 2024-08-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_contact_email1_remove_contact_email2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='programming_languages',
            new_name='programs',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='programming_skills',
            new_name='skills',
        ),
        migrations.AlterField(
            model_name='user',
            name='town',
            field=models.CharField(default='Москва', max_length=100, verbose_name='Город'),
        ),
    ]
