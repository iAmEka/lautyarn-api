from sqlalchemy.orm import Session
from ..models.user import User as UserModel
from ..schemas.user import UserCreate, UserUpdate
import uuid

def get_user(db: Session, user_id: uuid.UUID):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_user_by_uid(db: Session, uid: str):
    return db.query(UserModel).filter(UserModel.uid == uid).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: uuid.UUID, user: UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: uuid.UUID):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
