from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
import uuid

class DetailPesanan(Base):
    __tablename__ = "detail_pesanan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pesanan_id = Column(UUID(as_uuid=True), ForeignKey("pesanan.id"))
    rajutan_id = Column(UUID(as_uuid=True), ForeignKey("rajutan.id"))
    quantity = Column(Integer)

    pesanan = relationship("Pesanan", back_populates="detail")
    # rajutan relationship bisa kamu tambah sendiri jika mau
