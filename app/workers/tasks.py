import time
from .celery_app import celery_app


@celery_app.task(bind=True)
def send_welcome_email(self, email: str):
    time.sleep(5)  # имитация тяжёлой работы
    return f"Работа успешно выполнена! Отправлено сообщение на {email}"


@celery_app.task
def create_units(order_id: int, count: int):
    time.sleep(22)  # имитация работы

    # здесь в реальности запись в БД
    return {
        "order_id": order_id,
        "units_created": count,
    }


@celery_app.task
def create_boxes(order_id: int):
    time.sleep(9)

    return {
        "order_id": order_id,
        "boxes_created": 5,
    }


@celery_app.task
def finalize_order(results: list[dict]):
    order_id = results[0]["order_id"]
    return {
        "order_id": order_id,
        "status": "READY",
        "details": results,
    }
