# app/models/rajutan.py
from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from ..database import Base

class Rajutan(Base):
    __tablename__ = "rajutan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nama = Column(String, index=True)
    count_like = Column(Integer, default=0)
    count_favorite = Column(Integer, default=0)
    colorcode = Column(ARRAY(String))
    price = Column(Integer)
    url_gambar = Column(String, nullable=True)
    status = Column(String, default="ready")
    deskripsi = Column(String, nullable=True)

    # Foreign key ke type_rajutan
    id_type = Column(UUID(as_uuid=True), ForeignKey("type_rajutan.id"), nullable=False)

    # Relationship ke model type
    type_rajutan = relationship("TypeRajutan", back_populates="rajutans")
