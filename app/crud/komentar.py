# app/crud/komentar.py
from sqlalchemy.orm import Session
import uuid

# Import the SQLAlchemy ORM Model specifically
from ..models.komentar import KomentarProduk as KomentarProdukModel # Alias it to avoid naming conflicts

# Import the Pydantic Schemas specifically
from ..schemas.komentar import KomentarProdukCreate, KomentarProduk as KomentarProdukSchema # Alias KomentarProduk if needed

def get_komentar(db: Session, komentar_id: uuid.UUID):
    # Use the aliased KomentarProdukModel here
    return db.query(KomentarProdukModel).filter(KomentarProdukModel.id == komentar_id).first()

def get_rajutan_komentar(db: Session, rajutan_id: uuid.UUID, skip: int = 0, limit: int = 100):
    # Use the aliased KomentarProdukModel here
    return db.query(KomentarProdukModel).filter(KomentarProdukModel.id_rajutan == rajutan_id).offset(skip).limit(limit).all()

def create_komentar(db: Session, komentar: KomentarProdukCreate): # KomentarProdukCreate is a Pydantic Schema
    # Create an instance of the KomentarProdukModel (SQLAlchemy ORM model)
    db_komentar = KomentarProdukModel(**komentar.dict())
    db.add(db_komentar)
    db.commit()
    db.refresh(db_komentar)
    return db_komentar

def delete_komentar(db: Session, komentar_id: uuid.UUID):
    # Use the aliased KomentarProdukModel here
    db_komentar = db.query(KomentarProdukModel).filter(KomentarProdukModel.id == komentar_id).first()
    if db_komentar:
        db.delete(db_komentar)
        db.commit()
    return db_komentar