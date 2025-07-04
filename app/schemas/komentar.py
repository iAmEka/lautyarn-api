from pydantic import BaseModel
import uuid

class KomentarProdukBase(BaseModel):
    id_user: uuid.UUID
    id_rajutan: uuid.UUID
    pesan: str

class KomentarProdukCreate(KomentarProdukBase):
    pass

class KomentarProdukUpdate(BaseModel):
    pesan: str  # Hanya pesan yang bisa diubah

class KomentarProduk(KomentarProdukBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
