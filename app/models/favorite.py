from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from ..database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    id_rajutan = Column(UUID(as_uuid=True), ForeignKey("rajutan.id"))

    user = relationship("User")
    rajutan = relationship("Rajutan")
