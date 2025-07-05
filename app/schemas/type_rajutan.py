from pydantic import BaseModel
import uuid

class TypeRajutanBase(BaseModel):
    nama: str

class TypeRajutanCreate(TypeRajutanBase):
    pass

class TypeRajutanUpdate(TypeRajutanBase):
    pass

class TypeRajutan(TypeRajutanBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
