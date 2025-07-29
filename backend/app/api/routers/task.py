from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
import app.crud.task as crud_task
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(tags=["tasks"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TaskRead])
def read_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_task.read_tasks_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )


@router.get("/{task_id}", response_model=TaskRead)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_task.get_task_by_user(db, task_id, current_user.id)


@router.post("/", response_model=TaskRead)
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Set the user_id to the current authenticated user
    task.user_id = current_user.id
    return crud_task.create_task(db=db, task=task)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_task.update_task_by_user(
        db=db, task_id=task_id, task=task, user_id=current_user.id
    )


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_task.delete_task_by_user(
        db=db, task_id=task_id, user_id=current_user.id
    )
