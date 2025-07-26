from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
import uuid

class ItemCartBase(BaseModel):
    rajutan_id: uuid.UUID
    quantity: int = 1
    price_at_added: int
    status: Optional[str] = "in_cart"

    @validator("status")
    def validate_status(cls, v):
        allowed = {"in_cart", "checked_out", "removed"}
        if v not in allowed:
            raise ValueError(f"Status harus salah satu dari: {allowed}")
        return v

class ItemCartCreate(ItemCartBase):
    pass

class ItemCartUpdate(BaseModel):
    quantity: Optional[int] = None
    status: Optional[str] = None

    @validator("status")
    def validate_status(cls, v):
        allowed = {"in_cart", "checked_out", "removed"}
        if v is not None and v not in allowed:
            raise ValueError(f"Status harus salah satu dari: {allowed}")
        return v

class ItemCartResponse(ItemCartBase):
    id: uuid.UUID
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
