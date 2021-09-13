# Yellow Pages

## Проект Django REST API.

### Требования

- Указаны в **requirements.txt**

### Запуск проекта в dev-mode

- Установите и активируйте виртуальное окружение venv. [Подробнее](https://pythoner.name/documentation/tutorial/venv)
- Установите зависимости из **requirements.txt**

```python
pip install -r requirements.txt
```

- Запустите миграции (из папки с manage.py)

```python
python manage.py migrate
```

- Создайте суперпользователя:

```python
 python manage.py createsuperuser
```

- Запустите сервер

```python
 python manage.py runserver 
```
### Эндпоинты

- Базовый /api/v1/

#### Аутентификация
-  Получить токен /auth/token/ (в запросе email и password)

#### Общие (Все начинаются с базового)

- Организации **organizations/**
- Сотрудники **organizations/\<int:organization_id\>/employees/**
- Список редакторов организации **organizations/\<organization_id\>/editors/**
- Добавить редактора (не реализовано) **organizations/\<int:organization_id\>/add_editor/**
- Удалить редактора (не реализовано) **organizations/\<int:organization_id\>/remove_editor/**
- Список организаций, где я редактор или автор **my_org/**

### Не реализованные функции

- Глобальный поиск на эндпоинте search
- Добавление редектора для организации
- Удаление редактора у организации
