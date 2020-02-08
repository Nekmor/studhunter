# Generated by Django 3.0.3 on 2020-02-08 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64, verbose_name='Название работы')),
                ('num', models.IntegerField(verbose_name='Количество людей')),
                ('find', models.IntegerField(verbose_name='Найдено людей')),
                ('salary', models.IntegerField(verbose_name='Бюджет')),
                ('body', models.CharField(max_length=64, verbose_name='Описание работы')),
                ('date_end', models.DateTimeField(verbose_name='Когда нужно сделать')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
