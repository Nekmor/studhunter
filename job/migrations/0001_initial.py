# Generated by Django 2.2.10 on 2020-02-10 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Электронная почта')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('phone', phone_field.models.PhoneField(max_length=31, verbose_name='Телефонный номер')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, verbose_name='Название')),
                ('count_people', models.CharField(max_length=10, verbose_name='Количество людей')),
                ('find', models.CharField(blank=True, max_length=10, verbose_name='Найдено людей')),
                ('cost', models.CharField(max_length=100, verbose_name='Цена')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('execute_period', models.CharField(blank=True, max_length=20, verbose_name='Срок сдачи')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
