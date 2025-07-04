# app/crud/admin.py
from sqlalchemy.orm import Session
import uuid

# Impor Model ORM SQLAlchemy Admin yang BENAR (dari models)
from ..models.admin import Admin as AdminModel # <-- Beri alias untuk menghindari konflik nama

# Impor Skema Pydantic Admin (dari schemas)
from ..schemas.admin import AdminCreate, AdminUpdate, Admin as AdminSchema # <-- Beri alias

def get_admin(db: Session, admin_id: uuid.UUID):
    return db.query(AdminModel).filter(AdminModel.id == admin_id).first() # Gunakan AdminModel

def get_admin_by_email(db: Session, email: str):
    return db.query(AdminModel).filter(AdminModel.email == email).first() # Gunakan AdminModel

def get_admin_by_uid(db: Session, firebase_uid: str):
    return db.query(AdminModel).filter(AdminModel.firebase_uid == firebase_uid).first()


def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AdminModel).offset(skip).limit(limit).all() # Gunakan AdminModel

def create_admin(db: Session, admin: AdminCreate): # AdminCreate ini adalah skema Pydantic
    db_admin = AdminModel(**admin.dict()) # Buat instance dari AdminModel (ORM)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def update_admin(db: Session, admin_id: uuid.UUID, admin: AdminUpdate): # AdminUpdate ini adalah skema Pydantic
    db_admin = db.query(AdminModel).filter(AdminModel.id == admin_id).first() # Gunakan AdminModel
    if db_admin:
        for key, value in admin.dict(exclude_unset=True).items():
            setattr(db_admin, key, value)
        db.commit()
        db.refresh(db_admin)
    return db_admin

def delete_admin(db: Session, admin_id: uuid.UUID):
    db_admin = db.query(AdminModel).filter(AdminModel.id == admin_id).first() # Gunakan AdminModel
    if db_admin:
        db.delete(db_admin)
        db.commit()
    return db_admin