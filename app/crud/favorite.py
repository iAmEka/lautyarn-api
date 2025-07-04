# app/crud/favorite.py
from sqlalchemy.orm import Session
import uuid

# Impor Model ORM SQLAlchemy Favorite yang BENAR (dari models)
# Karena Favorite memiliki FK ke Customer dan Rajutan, kita juga perlu model mereka jika digunakan di CRUD Favorite
from ..models.favorite import Favorite as FavoriteModel
from ..models.customer import Customer as CustomerModel # Jika diperlukan untuk relasi/join di CRUD ini
from ..models.rajutan import Rajutan as RajutanModel   # Jika diperlukan untuk relasi/join di CRUD ini


# Impor Skema Pydantic Favorite (dari schemas)
from ..schemas.favorite import FavoriteCreate, Favorite as FavoriteSchema # Impor spesifik

def get_favorite(db: Session, favorite_id: uuid.UUID):
    return db.query(FavoriteModel).filter(FavoriteModel.id == favorite_id).first()

def get_customer_favorites(db: Session, customer_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(FavoriteModel).filter(FavoriteModel.id_customer == customer_id).offset(skip).limit(limit).all()

def create_favorite(db: Session, favorite: FavoriteCreate): # Gunakan FavoriteCreate langsung
    db_favorite = FavoriteModel(**favorite.dict()) # Gunakan FavoriteModel
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def delete_favorite(db: Session, favorite_id: uuid.UUID):
    db_favorite = db.query(FavoriteModel).filter(FavoriteModel.id == favorite_id).first()
    if db_favorite:
        db.delete(db_favorite)
        db.commit()
    return db_favorite