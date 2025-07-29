from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import HTTPException


def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, priority=task.priority, user_id=task.user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


def get_task_by_user(db: Session, task_id: int, user_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found for user")
    return task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.title = task.title or db_task.title
        db_task.priority = task.priority or db_task.priority
        db.commit()
        db.refresh(db_task)
    return db_task


def update_task_by_user(db: Session, task_id: int, task: TaskUpdate, user_id: int):
    db_task = get_task_by_user(db, task_id, user_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task:
        db_task.title = task.title or db_task.title
        db_task.priority = task.priority or db_task.priority
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"ok": True}


def delete_task_by_user(db: Session, task_id: int, user_id: int):
    db_task = get_task_by_user(db, task_id, user_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found for user")
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found for user")
    db.delete(db_task)
    db.commit()
    return {"ok": True}


def read_all_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()


def read_tasks_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()
    )
