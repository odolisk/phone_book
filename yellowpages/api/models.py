from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from .validators import UniquePhoneValidator


class User(AbstractUser):

    email = models.EmailField(
        'email',
        unique=True,
        help_text='Email адрес. Должен быть уникальным.',
        error_messages={
            'unique': 'Пользователь с таким Email уже существует.',
        })

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)


class Organization(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)
    address = models.TextField('Адрес', blank=True)
    description = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создано',
        related_name='organization_author')

    editors = models.ManyToManyField(
        User, related_name='organization_editors',
        blank=True, verbose_name='Редакторы')

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
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        related_name='employees',
        blank=True,
        null=True,
        verbose_name='Организация')

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
        validators=[phone_regex, UniquePhoneValidator],
        max_length=17,
        blank=True,
        null=True,
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
            models.Index(fields=('name', 'surname', 'middlename',
                                 'work_phone', 'personal_phone', 'fax')),
        ]
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'surname', 'middlename', 'organization'),
                name='FIO'),
        )

    @property
    def full_name(self):
        fname = f'{self.surname} {self.name} {self.middlename}'.strip()
        return fname

    def clean(self):
        if not (self.personal_phone or self.work_phone or self.fax):
            raise ValidationError('Хотя бы один телефон обязателен')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.surname + ' ' + self.name
