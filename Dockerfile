# Использую базовый образ Python
FROM python:3.9

# Установка переменной окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создание директории приложения в контейнере
RUN mkdir /code

# Установка рабочей директории в контейнере
WORKDIR /code

# Копирование зависимостей и установка их
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта в контейнер
COPY . /code/

# Запуск миграций
RUN python manage.py migrate

# Задание переменной окружения для пути к статическим файлам
ENV STATIC_URL /static/
ENV STATIC_ROOT /code/static/

# Запуск команды для запуска сервера Django и бота
CMD python manage.py runserver 0.0.0.0:8000 & python manage.py bot