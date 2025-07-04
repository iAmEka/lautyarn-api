from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from ..schemas.komentar import KomentarProduk, KomentarProdukCreate, KomentarProdukUpdate
from ..crud.komentar import (
    create_komentar,
    get_komentar,
    get_all_komentar,
    get_rajutan_komentar,
    update_komentar,
    delete_komentar,
)
from ..database import get_db

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)

@router.post("/", response_model=KomentarProduk)
def create_komentar_endpoint(komentar: KomentarProdukCreate, db: Session = Depends(get_db)):
    return create_komentar(db, komentar)

@router.get("/", response_model=List[KomentarProduk])
def get_all_komentar_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_komentar(db, skip, limit)

@router.get("/{komentar_id}", response_model=KomentarProduk)
def get_komentar_by_id_endpoint(komentar_id: uuid.UUID, db: Session = Depends(get_db)):
    komentar = get_komentar(db, komentar_id)
    if komentar is None:
        raise HTTPException(status_code=404, detail="Komentar tidak ditemukan")
    return komentar

@router.get("/rajutan/{rajutan_id}", response_model=List[KomentarProduk])
def get_komentar_by_rajutan_endpoint(rajutan_id: uuid.UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_rajutan_komentar(db, rajutan_id, skip, limit)

@router.put("/{komentar_id}", response_model=KomentarProduk)
def update_komentar_endpoint(komentar_id: uuid.UUID, komentar_data: KomentarProdukUpdate, db: Session = Depends(get_db)):
    komentar = update_komentar(db, komentar_id, komentar_data)
    if komentar is None:
        raise HTTPException(status_code=404, detail="Komentar tidak ditemukan")
    return komentar

@router.delete("/{komentar_id}")
def delete_komentar_endpoint(komentar_id: uuid.UUID, db: Session = Depends(get_db)):
    komentar = delete_komentar(db, komentar_id)
    if komentar is None:
        raise HTTPException(status_code=404, detail="Komentar tidak ditemukan")
    return {"message": "Komentar berhasil dihapus"}
