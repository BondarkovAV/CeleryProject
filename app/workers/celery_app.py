from app.config import settings
from celery import Celery


celery_app = Celery(
    "worker",
    broker=settings.rabbitmq.dsn.encoded_string(),
    backend=settings.redis.dsn.encoded_string(),
)
celery_app.autodiscover_tasks(
    ["app.workers"],
)
celery_app.conf.task_routes = {
    "app.workers.tasks.*": {"queue": "default"},
}
