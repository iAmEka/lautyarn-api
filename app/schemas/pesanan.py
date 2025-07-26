from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime
from .detail_pesanan import DetailPesananCreate, DetailPesananResponse

class PesananCreate(BaseModel):
    user_id: UUID
    detail: List[DetailPesananCreate]

class PesananResponse(BaseModel):
    id: UUID
    user_id: UUID
    tanggal_pesanan: datetime
    status: str
    detail: List[DetailPesananResponse]

    class Config:
        orm_mode = True
