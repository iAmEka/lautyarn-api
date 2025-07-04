# app/schemas/admin.py
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class AdminBase(BaseModel):
    nama: str
    email: EmailStr
    username: str
    nomor_telepon: str
    alamat: str
    firebase_uid: str


class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    nama: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    nomor_telepon: Optional[str] = None
    alamat: Optional[str] = None

class Admin(AdminBase):
    id: uuid.UUID

    class Config:
        from_attributes = True