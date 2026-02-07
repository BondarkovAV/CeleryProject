from celery import Celery


celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0",
)
celery_app.autodiscover_tasks(
    ["app.workers"],
)
celery_app.conf.task_routes = {
    "app.workers.tasks.*": {"queue": "default"},
}
