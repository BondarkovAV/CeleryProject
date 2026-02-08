from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base
from app.config import settings


DATABASE_URL = (f"postgresql+asyncpg://"
                f"{settings.postgres_user}:{settings.postgres_password}@db:5432/{settings.postgres_db}")
print(DATABASE_URL)

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.database.echo,
    pool_size=settings.database.pool_size,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=settings.database.expire_on_commit,
)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
