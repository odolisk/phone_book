# Generated by Django 3.2.7 on 2021-09-01 08:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('middlename', models.CharField(blank=True, max_length=128, verbose_name='Отчество')),
                ('position', models.CharField(blank=True, max_length=128, verbose_name='Должность')),
                ('work_phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')])),
                ('personal_phone', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')])),
                ('fax', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('surname', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ('name',),
            },
        ),
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['name'], name='api_organiz_name_d3d16b_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['name', 'surname', 'middlename'], name='api_employe_name_6e47cf_idx'),
        ),
    ]