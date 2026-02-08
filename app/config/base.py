from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, Field, RedisDsn, AmqpDsn


class AppSettings(BaseSettings):
    name: str = "app"
    title: str = ""
    version: str = ""
    api_prefix: str = ""
    env: str = Field(default="dev", validation_alias="ENV")
    debug: bool = True


class LoggerSettings(BaseSettings):
    level: str = "INFO"


class DatabaseSettings(BaseSettings):
    echo: bool = True
    expire_on_commit: bool = True
    pool_size: int = 10


class RedisSettings(BaseSettings):
    dsn: RedisDsn = "redis://redis:6379/1"


class RabbitmqSettings(BaseSettings):
    dsn: AmqpDsn = "amqp://guest:guest@rabbitmq:5672//"


class CelerySettings(BaseSettings):
    task_serializer: str = "json"
    accept_content: list[str] = ["json"]


class Settings(BaseSettings):
    app: AppSettings
    database: DatabaseSettings
    redis: RedisSettings
    rabbitmq: RabbitmqSettings
    celery: CelerySettings
    logger: LoggerSettings
    tag: str = 'latest'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_db: str = 'postgres'
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore",
    )


