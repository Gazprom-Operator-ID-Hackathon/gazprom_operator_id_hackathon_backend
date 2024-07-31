import re
from django.core.exceptions import ValidationError

def validate_links(value):
    """Валидатор для поля links"""
    if len(value) > 3:
        raise ValidationError('Можно добавить не более трех ссылок.')

def validate_phone_numbers(value):
    """Валидатор для поля phone_numbers"""
    phone_regex = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    if not isinstance(value, list):
        raise ValidationError('Номера телефонов должны быть в виде списка.')
    if len(value) > 2:
        raise ValidationError('Можно добавить не более двух номеров телефонов.')
    for phone in value:
        if not phone_regex.match(phone):
            raise ValidationError(f'Неверный формат номера телефона: {phone}')

def validate_emails(value):
    """Валидатор для поля emails"""
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not isinstance(value, list):
        raise ValidationError('Адреса электронной почты должны быть в виде списка.')
    if len(value) > 2:
        raise ValidationError('Можно добавить не более двух адресов электронной почты.')
    for email in value:
        if not email_regex.match(email):
            raise ValidationError(f'Неверный формат адреса электронной почты: {email}')

def validate_hashtags(value):
    """Валидатор для поля hashtags"""
    hashtag_regex = re.compile(r'^#[\w-]+$')
    if not isinstance(value, list):
        raise ValidationError('Хештеги должны быть в виде списка.')
    for hashtag in value:
        if not hashtag_regex.match(hashtag):
            raise ValidationError(f'Неверный формат хештега: {hashtag}')