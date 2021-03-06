# Generated by Django 4.0.6 on 2022-07-05 11:17

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support_app', '0003_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор сообщения'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Active', 'Активно'), ('Solved', 'Решено'), ('Unsolved', 'Не решено'), ('Frozen', 'Заморожено')], default='Active', max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Тема'),
        ),
    ]
