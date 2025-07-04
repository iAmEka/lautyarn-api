# app/models/user.py
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uid = Column(String, unique=True, index=True)  # Firebase UID
    email = Column(String, unique=True, index=True)
    nama = Column(String)
    username = Column(String, unique=True)
    nomor_telepon = Column(String)
    alamat = Column(String)
    role = Column(String)  # 'admin' atau 'customer'
