# Generated by Django 4.2.6 on 2023-10-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_claim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.ManyToManyField(blank=True, default='Новая', null=True, to='core.status'),
        ),
    ]
