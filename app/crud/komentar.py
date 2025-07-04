from sqlalchemy.orm import Session
import uuid
from ..models.komentar import KomentarProduk as KomentarProdukModel
from ..schemas.komentar import KomentarProdukCreate, KomentarProdukUpdate

def get_komentar(db: Session, komentar_id: uuid.UUID):
    return db.query(KomentarProdukModel).filter(KomentarProdukModel.id == komentar_id).first()

def get_all_komentar(db: Session, skip: int = 0, limit: int = 100):
    return db.query(KomentarProdukModel).offset(skip).limit(limit).all()

def get_rajutan_komentar(db: Session, rajutan_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(KomentarProdukModel).filter(KomentarProdukModel.id_rajutan == rajutan_id).offset(skip).limit(limit).all()

def create_komentar(db: Session, komentar: KomentarProdukCreate):
    db_komentar = KomentarProdukModel(**komentar.dict())
    db.add(db_komentar)
    db.commit()
    db.refresh(db_komentar)
    return db_komentar

def update_komentar(db: Session, komentar_id: uuid.UUID, komentar_data: KomentarProdukUpdate):
    komentar = db.query(KomentarProdukModel).filter(KomentarProdukModel.id == komentar_id).first()
    if komentar is None:
        return None
    komentar.pesan = komentar_data.pesan
    db.commit()
    db.refresh(komentar)
    return komentar

def delete_komentar(db: Session, komentar_id: uuid.UUID):
    komentar = db.query(KomentarProdukModel).filter(KomentarProdukModel.id == komentar_id).first()
    if komentar:
        db.delete(komentar)
        db.commit()
    return komentar
