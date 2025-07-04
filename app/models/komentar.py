from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from ..database import Base

class KomentarProduk(Base):
    __tablename__ = "komentar_produk"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_customer = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    id_rajutan = Column(UUID(as_uuid=True), ForeignKey("rajutan.id"))
    pesan = Column(String)

    customer = relationship("Customer")
    rajutan = relationship("Rajutan") 
