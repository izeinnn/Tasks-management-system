from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
import app.crud.user as crud_user
from app.schemas.user import UserCreate, UserRead, UserUpdate, UserOut
from app.core.deps import get_current_user
from app.models.user import User


router = APIRouter(tags=["users"])


# as example, this route is protected by the get_current_user dependency
# which means that the user must be authenticated to access it.
@router.get(
    "/", response_model=list[UserRead], dependencies=[Depends(get_current_user)]
)
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud_user.read_all_users(db=db, skip=skip, limit=limit)


@router.get(
    "/{user_id}", response_model=UserOut, dependencies=[Depends(get_current_user)]
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.read_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud_user.read_user_by_id(db, user_id)


@router.post("/", response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)


@router.put(
    "/{user_id}", response_model=UserOut, dependencies=[Depends(get_current_user)]
)
def update_user_route(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}", dependencies=[Depends(get_current_user)])
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user(db=db, user_id=user_id)
