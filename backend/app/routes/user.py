from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut, UserUpdate
from database.database import get_db

user_router = APIRouter()

@user_router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(email=user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user_router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# READ - 단일 유저
@user_router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# READ - 전체 유저
@user_router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# UPDATE
@user_router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, update_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

# DELETE
@user_router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}