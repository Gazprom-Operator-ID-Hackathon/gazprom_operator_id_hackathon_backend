import re
from django.core.exceptions import ValidationError

def validate_hashtags(value):
    """Валидатор для поля hashtags"""
    hashtag_regex = re.compile(r'^#[\w-]+$')
    if not isinstance(value, list):
        raise ValidationError('Хештеги должны быть в виде списка.')
    for hashtag in value:
        if not hashtag_regex.match(hashtag):
            raise ValidationError(f'Неверный формат хештега: {hashtag}')