# CeleryProject

Это простой работающий проект с использованием Celery, RabbitMQ, Redis, PostgreSQL, Docker.

![Статус сборки](https://img.shields.io/badge/build-passing-brightgreen) ![Версия](https://img.shields.io/badge/version-1.0.0-blue) ![Лицензия](https://img.shields.io/badge/license-MIT-green) [![Стандарты кода](https://img.shields.io/badge/code%20style-standard-brightgreen.svg)](https://standardjs.com)

## Технологии

- **FastAPI** - современный веб-фреймворк
- **Celery** - распределенная очередь задач
- **PostgreSQL** - реляционная база данных
- **Redis** - кэш и бэкенд для результатов Celery
- **RabbitMQ** - брокер сообщений для Celery
- **SQLAlchemy 2.0** - ORM
- **Docker** - контейнеризация


## 📋 Оглавление

- [Установка](#установка)


## 🚀 Установка

### Предварительные требования

- Docker

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/BondarkovAV/CeleryProject.git
cd CeleryProject
```
2. Клонируйте репозиторий:
```bash
cp .env.example .env
cp .env.example .env.dev
cp .env.example .env.prod
```
3. Запуск:
```bash
# Разработка -dev (автоматически подхватит override)
docker-compose up -d
```
```bash
# Продакшен (использует .prod файл)
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
```bash
# Сборка и запуск
ENV=prod docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```