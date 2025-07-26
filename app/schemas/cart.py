from pydantic import BaseModel
from typing import List
import uuid
from .item_cart import ItemCartResponse, ItemCartCreate

class CartBase(BaseModel):
    user_id: uuid.UUID

class CartCreate(CartBase):
    items: List[ItemCartCreate]

class CartResponse(CartBase):
    id: uuid.UUID
    items: List[ItemCartResponse]

    class Config:
        orm_mode = True
