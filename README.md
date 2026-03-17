# BookShelf — Платформа за рецензии на книги

Django уеб приложение за управление и рецензиране на книги.

## Инсталация

1. Клонирай репото: `git clone <url>`
2. Активирай venv: `python -m venv venv && source venv/bin/activate`
3. Инсталирай зависимости: `pip install -r requirements.txt`
4. Създай `.env` файл по примера в `.env.example`
5. Създай PostgreSQL база: `createdb bookshelf_db`
6. Приложи миграции: `python manage.py migrate`
7. Стартирай: `python manage.py runserver`

## Environment Variables

Създай `.env` файл със следните стойности:

| Променлива | Описание |
|------------|----------|
| SECRET_KEY | Django секретен ключ |
| DB_NAME | Име на базата данни |
| DB_USER | PostgreSQL потребител |
| DB_PASSWORD | PostgreSQL парола |
| DB_HOST | Хост (default: localhost) |
| DB_PORT | Порт (default: 5432) |

## Създаване на администратор
```
python manage.py createsuperuser
```

## Технологии

- Django 6.0
- PostgreSQL
- Bootstrap 5
# bookshelf-project
# bookshelf-project
# bookshelf-project
