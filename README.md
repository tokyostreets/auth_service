# auth_service
Сервис Авторизации на FastAPI


# Технологии
Python 3.12
FastAPI & Uvicorn
PostgreSQL 16
SQLAlchemy & Alembic
Docker & Docker Compose
Pydantic V2
JWT для аутентификации

# Были выполнены задачи

Регистрация пользователей с безопасным хешированием паролей на стороне БД (pgcrypto).
Аутентификация и выдача JWT токенов.
Защищенный эндпоинт для получения данных о текущем пользователе.

# .env Example:

POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=db

DATABASE_URL=postgresql://POSTGRES_USER:POSTGRES_PASSWORD@HOST:PORT/db

SECRET_KEY=SECRET_KEY
ALGORITHM=HS256 
ACCESS_TOKEN_EXPIRE_MINUTES=30

Не забудьте применить миграции при запуске: docker-compose exec web alembic upgrade head
