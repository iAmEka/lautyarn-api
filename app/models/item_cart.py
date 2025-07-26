from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from ..database import Base

class ItemCart(Base):
    __tablename__ = "item_cart"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cart_id = Column(UUID(as_uuid=True), ForeignKey("cart.id"), nullable=False)
    rajutan_id = Column(UUID(as_uuid=True), ForeignKey("rajutan.id"), nullable=False)
    quantity = Column(Integer, default=1)
    price_at_added = Column(Integer)
    status = Column(String, default="in_cart")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    cart = relationship("Cart", back_populates="items")
    # rajutan relationship kalau mau:
    # rajutan = relationship("Rajutan")
