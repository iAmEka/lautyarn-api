# app/models/rajutan.py
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..database import Base

class Rajutan(Base):
    __tablename__ = "rajutan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nama = Column(String, index=True)
    count_like = Column(Integer, default=0)
    count_favorite = Column(Integer, default=0)
    colorcode = Column(ARRAY(String)) # Array of strings
    price = Column(Integer)
    url_gambar = Column(String, nullable=True) # Tambahkan baris ini