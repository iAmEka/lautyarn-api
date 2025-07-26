from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ..database import get_db
from ..crud.pesanan import create_pesanan, get_all_pesanan
from ..schemas.pesanan import PesananCreate, PesananResponse

router = APIRouter(prefix="/pesanan", tags=["Pesanan"])

@router.post("/", response_model=PesananResponse)
def buat_pesanan(pesanan_data: PesananCreate, db: Session = Depends(get_db)):
    return create_pesanan(db, pesanan_data)

@router.get("/", response_model=List[PesananResponse])
def ambil_semua_pesanan(db: Session = Depends(get_db)):
    return get_all_pesanan(db)
