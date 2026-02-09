#!/bin/sh
set -e
echo "Update database tables from alembic"
alembic upgrade head
# Запускаем FastAPI приложение
echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
