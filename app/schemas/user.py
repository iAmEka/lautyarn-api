# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserBase(BaseModel):
    uid: str
    email: EmailStr
    nama: str
    username: str
    nomor_telepon: str
    alamat: str
    role: str  # 'admin' atau 'customer'

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nama: Optional[str]
    username: Optional[str]
    nomor_telepon: Optional[str]
    alamat: Optional[str]
    role: Optional[str]

class User(UserBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
