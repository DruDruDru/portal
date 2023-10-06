from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True, null=True)
    username = models.CharField('Логин', max_length=60, unique=True)

    def __str__(self):
        return self.username



