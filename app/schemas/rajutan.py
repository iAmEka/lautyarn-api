from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime
import uuid
from .type_rajutan import TypeRajutan

class RajutanBase(BaseModel):
    nama: str
    count_like: int = 0
    count_favorite: int = 0
    colorcode: List[str]
    price: int
    url_gambar: Optional[str] = None
    status: Optional[str] = "ready"
    deskripsi: Optional[str] = None
    id_type: uuid.UUID

    bahan: Optional[List[str]] = []
    pengrajin: Optional[str] = None
    ukuran: Optional[str] = None
    lama_pengerjaan: Optional[str] = None

    @validator("status")
    def validate_status(cls, v):
        allowed = {"ready", "pre_order"}
        if v not in allowed:
            raise ValueError(f"Status harus salah satu dari: {allowed}")
        return v


class RajutanCreate(RajutanBase):
    pass

class RajutanUpdate(BaseModel):
    nama: Optional[str] = None
    count_like: Optional[int] = None
    count_favorite: Optional[int] = None
    colorcode: Optional[List[str]] = None
    price: Optional[int] = None
    url_gambar: Optional[str] = None
    status: Optional[str] = None
    deskripsi: Optional[str] = None
    id_type: Optional[uuid.UUID] = None

    bahan: Optional[List[str]] = None
    pengrajin: Optional[str] = None
    ukuran: Optional[str] = None
    lama_pengerjaan: Optional[str] = None


    @validator("status")
    def validate_status(cls, v):
        allowed = {"ready", "pre_order"}
        if v is not None and v not in allowed:
            raise ValueError(f"Status harus salah satu dari: {allowed}")
        return v

class Rajutan(RajutanBase):
    id: uuid.UUID
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class RajutanWithType(Rajutan):
    type_rajutan: Optional[TypeRajutan]

    class Config:
        from_attributes = True
