# Generated by Django 3.2.7 on 2021-09-01 08:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization', to='api.organization', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fax',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')], verbose_name='Факс'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personal_phone',
            field=models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')], verbose_name='Личный телефон'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера: "+00000000000".Максимум - 15 символов (+71234567890).', regex='^\\+?1?\\d{9,15}$')], verbose_name='Рабочий телефон'),
        ),
    ]