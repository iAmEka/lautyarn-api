from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
import uuid
from datetime import datetime

class Pesanan(Base):
    __tablename__ = "pesanan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    tanggal_pesanan = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="menunggu")

    detail = relationship("DetailPesanan", back_populates="pesanan", cascade="all, delete-orphan")
