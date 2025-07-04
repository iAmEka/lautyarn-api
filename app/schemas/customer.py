from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class CustomerBase(BaseModel):
    nama: str
    email: EmailStr
    username: str
    nomor_telepon: str
    alamat: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    nama: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    nomor_telepon: Optional[str] = None
    alamat: Optional[str] = None

class Customer(CustomerBase):
    id: uuid.UUID

    class Config:
        from_attributes = True  
