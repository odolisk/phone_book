from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models


User = get_user_model()


class Organization(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)
    address = models.TextField('Адрес', blank=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)
        indexes = [
            models.Index(fields=('name',)),
        ]

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField('Имя', max_length=128)
    surname = models.CharField('Фамилия', max_length=128)
    middlename = models.CharField('Отчество', max_length=128, blank=True)
    position = models.CharField('Должность', max_length=128, blank=True)
    organization = models.ForeignKey(Organization,
                                     on_delete=models.SET_NULL,
                                     blank=False,
                                     null=True,
                                     verbose_name='Организация',
                                     related_name='employees')

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{8,15}$',
        message='Формат телефонного номера: "+00000000000".'
                'Максимум - 15 цифр (+71234567890).')
    work_phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        verbose_name='Рабочий телефон'
        )
    personal_phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        unique=True,
        verbose_name='Личный телефон')
    fax = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        verbose_name='Факс')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('surname', 'name',)
        indexes = [
            models.Index(fields=('name', 'surname', 'middlename')),
        ]

    def __str__(self):
        return self.surname + ' ' + self.name

    @property
    def get_full_name(self):
        fname = f'{self.surname} {self.name} {self.middlename}'.strip()
        return fname