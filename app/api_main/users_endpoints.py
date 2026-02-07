from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.maindb.database import get_session
from app.maindb.models import User
from app.schemas import UserCreate
from app.workers.tasks import send_welcome_email


router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    user = User(email=data.email)
    session.add(user)
    await session.commit()

    task = send_welcome_email.delay(data.email)

    return {"status": "created", "email": data.email, "celery_task_id": task.id}