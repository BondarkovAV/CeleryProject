from fastapi import APIRouter
from celery.result import AsyncResult
from app.workers.celery_app import celery_app


router = APIRouter(prefix="/celery")


@router.get("/{celery_task_id}")
def get_task_status(celery_task_id: str):
    result = AsyncResult(celery_task_id, app=celery_app)

    return {
        "task_id": celery_task_id,
        "status": result.status,
        "result": result.result if result.successful() else None,
    }


@router.get("/{workflow_id}")
def get_workflow_status(workflow_id: str):
    result = AsyncResult(workflow_id, app=celery_app)

    return {
        "workflow_id": workflow_id,
        "status": result.status,
        "result": result.result if result.successful() else None,
    }
