from pydantic import BaseModel
import uuid

class FavoriteBase(BaseModel):
    id_user: uuid.UUID
    id_rajutan: uuid.UUID

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
