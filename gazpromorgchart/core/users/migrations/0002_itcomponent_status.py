# Generated by Django 4.2.4 on 2024-08-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itcomponent',
            name='status',
            field=models.CharField(choices=[('active', 'Активный'), ('inactive', 'Неактивный')], default='active', max_length=10, verbose_name='Статус'),
        ),
    ]
