from django.db import models
from django.shortcuts import reverse
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


# ошибка - 1 , норма - 0
def validate_image_size(value):
    if value:
        if value.size > 2 * 1024 * 1024:  # Проверка на размер файла менее 2 МБ
            return 1
    return 0


class Claim(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category, help_text='Change your category')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    who_created = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    STATUS = (
        ('п', 'Принято в работу'),
        ('в', 'Выполнено'),
        ('н', 'Новая'),
    )

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='н')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('delete_claim', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('update_claim', args=[str(self.id)])

