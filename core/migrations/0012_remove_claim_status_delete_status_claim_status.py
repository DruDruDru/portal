# Generated by Django 4.2.6 on 2023-10-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_claim_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='claim',
            name='status',
            field=models.CharField(blank=True, choices=[('п', 'Принято в работу'), ('в', 'Выполнено'), ('н', 'Новая')], default='н', max_length=1),
        ),
    ]
