# Blogicum

## Описание проекта
Blogicum — это учебный проект, реализованный в рамках курса Python-разработчик  
(Бэкэнд на Django) на платформе Яндекс.Практикум.  
В проекте реализован блог с публикациями, категориями, локациями и фильтрацией по авторам.

## Стек технологий
- Python 3.12  
- Django 5.1.1  
- HTML, CSS (шаблоны Django)  
- pytest (для тестирования)  
- Flake8, Mypy (для проверки кода)

## Развертывание проекта

1. Клонирование репозитория:
git clone https://github.com/pyryanova/django-sprint3.git
cd django-sprint3

2. Создание виртуального окружения:
python -m venv venv  
source venv/bin/activate  (Для macOS/Linux)  
venv\Scripts\activate  (Для Windows)  

3. Установка зависимостей:
pip install -r requirements.txt  

4. Применение миграций и загрузка тестовых данных:
python manage.py migrate
python manage.py loaddata db.json

5. Запуск сервера:
python manage.py runserver  
После запуска сервер будет доступен по адресу:  
http://127.0.0.1:8000/

## Тестирование
Для запуска тестов используйте команду:
pytest

## Автор
Ольга Пырьянова (https://github.com/pyryanova)
