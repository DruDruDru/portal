
from django.core.exceptions import ValidationError


def validate_checkbox(value):
    if not value:
        raise ValidationError('Пожалуйста, подтвердите согласие на обработку персональных данных.')
