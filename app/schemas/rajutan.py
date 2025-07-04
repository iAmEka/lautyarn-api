# app/schemas/rajutan.py
from pydantic import BaseModel, HttpUrl # Import HttpUrl jika ingin validasi URL yang lebih ketat
from typing import List, Optional
import uuid

class RajutanBase(BaseModel):
    nama: str
    count_like: int = 0
    count_favorite: int = 0
    colorcode: List[str]
    price: int
    url_gambar: Optional[str] = None # Atau HttpUrl jika Anda menggunakan Pydantic v2+ dan ingin validasi ketat

class RajutanCreate(RajutanBase):
    pass

class RajutanUpdate(BaseModel):
    nama: Optional[str] = None
    count_like: Optional[int] = None
    count_favorite: Optional[int] = None
    colorcode: Optional[List[str]] = None
    price: Optional[int] = None
    url_gambar: Optional[str] = None # Tambahkan baris ini

class Rajutan(RajutanBase):
    id: uuid.UUID

    class Config:
        from_attributes = True