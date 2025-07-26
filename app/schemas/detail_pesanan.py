from pydantic import BaseModel
from uuid import UUID

class DetailPesananCreate(BaseModel):
    rajutan_id: UUID
    quantity: int

class DetailPesananResponse(BaseModel):
    rajutan_id: UUID
    quantity: int

    class Config:
        orm_mode = True
