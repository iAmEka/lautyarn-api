from sqlalchemy.orm import Session
from ..schemas.rajutan import RajutanCreate, RajutanUpdate
from ..models.rajutan import Rajutan
import uuid

def get_rajutan(db: Session, rajutan_id: uuid.UUID):
    return db.query(Rajutan).filter(Rajutan.id == rajutan_id).first()

def get_all_rajutan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Rajutan).offset(skip).limit(limit).all()

def create_rajutan(db: Session, rajutan: RajutanCreate):
    db_rajutan = Rajutan(**rajutan.dict())
    db.add(db_rajutan)
    db.commit()
    db.refresh(db_rajutan)
    return db_rajutan

def update_rajutan(db: Session, rajutan_id: uuid.UUID, rajutan: RajutanUpdate):
    db_rajutan = db.query(Rajutan).filter(Rajutan.id == rajutan_id).first()
    if db_rajutan:
        for key, value in rajutan.dict(exclude_unset=True).items():
            setattr(db_rajutan, key, value)
        db.commit()
        db.refresh(db_rajutan)
    return db_rajutan

def delete_rajutan(db: Session, rajutan_id: uuid.UUID):
    db_rajutan = db.query(Rajutan).filter(Rajutan.id == rajutan_id).first()
    if db_rajutan:
        db.delete(db_rajutan)
        db.commit()
    return db_rajutan
