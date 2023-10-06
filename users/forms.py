from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser
from django.core.validators import RegexValidator, MaxLengthValidator
from .validators import validate_checkbox


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        max_length=30,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9-]+$',
                'Логин может содержать только латинские символы и дефис.'
            ),
            MaxLengthValidator(30),
        ]
    )

    last_name = forms.CharField(
        label="Фамилия",
        max_length=30,
        validators=[
            RegexValidator(
                r'^[а-яА-ЯёЁ\s-]+$',
                'Фамилия может содержать только кириллицу, дефис и пробелы.'
            ),
            MaxLengthValidator(30),
        ]
    )

    first_name = forms.CharField(
        label="Имя",
        max_length=30,
        validators=[
            RegexValidator(
                r'^[а-яА-ЯёЁ\s-]+$',
                'Имя может содержать только кириллицу, дефис и пробелы.'
            ),
            MaxLengthValidator(30),
        ]
    )

    patronymic = forms.CharField(
        label="Отчество",
        max_length=30,
        validators=[
            RegexValidator(
                r'^[а-яА-ЯёЁ\s-]+$',
                'Отчество может содержать только кириллицу, дефис и пробелы.'
            ),
            MaxLengthValidator(30),
        ]
    )

    agree_checkbox = forms.BooleanField(
        required=True,
        label='Я даю согласие на обработку персональных данных',
        validators=[validate_checkbox]
    )

    class Meta:
        model = CustomUser
        #
        fields = ('last_name', 'first_name', 'patronymic', 'username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'patronymic', 'username', 'email')


