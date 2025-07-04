from pydantic import BaseModel
import uuid

class KomentarProdukBase(BaseModel):
    id_customer: uuid.UUID
    id_rajutan: uuid.UUID
    pesan: str

class KomentarProdukCreate(KomentarProdukBase):
    pass

class KomentarProduk(KomentarProdukBase):
    id: uuid.UUID

    class Config:
        from_attributes = True 
