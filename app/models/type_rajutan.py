from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from ..database import Base

class TypeRajutan(Base):
    __tablename__ = "type_rajutan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nama = Column(String, unique=True, nullable=False)

    # Relasi ke Rajutan
    rajutans = relationship("Rajutan", back_populates="type_rajutan")
