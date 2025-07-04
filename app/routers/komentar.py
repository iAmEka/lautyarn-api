# app/routers/komentar.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

# Import schemas
from ..schemas.komentar import KomentarProduk, KomentarProdukCreate
# Pastikan Anda mengimpor fungsi CRUD secara spesifik seperti ini:
from ..crud.komentar import create_komentar, get_komentar, get_rajutan_komentar, delete_komentar
from ..database import get_db

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)

@router.post("/", response_model=KomentarProduk)
# Saya mengubah nama fungsi menjadi create_komentar_endpoint untuk kejelasan, tapi tidak wajib.
def create_komentar_endpoint(komentar: KomentarProdukCreate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    return create_komentar(db=db, komentar=komentar) # Panggil langsung create_komentar

@router.get("/rajutan/{rajutan_id}", response_model=List[KomentarProduk])
def read_rajutan_komentar_endpoint(rajutan_id: uuid.UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    komentars = get_rajutan_komentar(db, rajutan_id=rajutan_id, skip=skip, limit=limit) # Panggil langsung get_rajutan_komentar
    return komentars

@router.delete("/{komentar_id}")
def delete_komentar_endpoint(komentar_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_komentar = delete_komentar(db, komentar_id=komentar_id) # Panggil langsung delete_komentar
    if db_komentar is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}