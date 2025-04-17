# Базовый образ с Python 3.12
FROM python:3.12-slim-bookworm

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==$POETRY_VERSION"

# Рабочая директория
WORKDIR /app

# Сначала копируем только файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . .

# Порт приложения
EXPOSE 8000

# Команда запуска
CMD ["granian", "--host", "0.0.0.0", "--port", "8000", "--interface", "asgi", "app.asgi:app"]