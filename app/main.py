from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from .maindb.database import Base, engine
from .api_main import celery_endpoints, orders_endpoints, users_endpoints
from .config import settings


logging.basicConfig(level=settings.logger.level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan контекст для управления жизненным циклом приложения"""
    # Создание таблиц при старте
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Таблицы базы данных созданы/проверены")
    except Exception as e:
        logger.error(f"❌ Ошибка при создании таблиц: {e}")

    yield

    # Завершение работы
    logger.info("Приложение завершает работу...")


app = FastAPI(
    title=settings.app.name,
    description=settings.app.title,
    version=settings.app.version,
    lifespan=lifespan
)

app.include_router(celery_endpoints.router, prefix=settings.app.api_prefix, tags=["celery"])
app.include_router(orders_endpoints.router, prefix=settings.app.api_prefix, tags=["orders"])
app.include_router(users_endpoints.router, prefix=settings.app.api_prefix, tags=["users"])


@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в демонстрационное приложение!",
        "docs": "/docs",
        "redoc": "/redoc",
        "health_check": "/api/health"
    }


@app.get("/health")
async def health():
    return {"status": "ok", "version": app.version}


