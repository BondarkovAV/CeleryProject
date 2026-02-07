from fastapi import APIRouter
from celery import chord, group
from app.workers.tasks import create_units, create_boxes, finalize_order


router = APIRouter(prefix="/orders")


@router.post("/")
async def create_order(units_count: int):
    # 1️⃣ создать заказ в БД
    order_id = 1  # допустим, получили ID

    # 2️⃣ собрать workflow
    workflow = chord(
        group(
            create_units.s(order_id, units_count),
            create_boxes.s(order_id),
        )
    )(finalize_order.s())

    return {
        "order_id": order_id,
        "workflow_id": workflow.id,
    }


