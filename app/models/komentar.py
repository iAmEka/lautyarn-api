from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from ..database import Base

class KomentarProduk(Base):
    __tablename__ = "komentar_produk"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    id_rajutan = Column(UUID(as_uuid=True), ForeignKey("rajutan.id"), nullable=False)
    pesan = Column(String, nullable=False)

    user = relationship("User")
    rajutan = relationship("Rajutan")
