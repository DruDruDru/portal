# Generated by Django 3.2.22 on 2023-10-06 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_alter_claim_who_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='who_created',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
