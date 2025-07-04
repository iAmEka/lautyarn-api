from sqlalchemy.orm import Session
import uuid
from ..models.favorite import Favorite as FavoriteModel
from ..models.rajutan import Rajutan as RajutanModel
from ..schemas.favorite import FavoriteCreate

def get_favorite(db: Session, favorite_id: uuid.UUID):
    return db.query(FavoriteModel).filter(FavoriteModel.id == favorite_id).first()

def get_user_favorites(db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(FavoriteModel).filter(FavoriteModel.id_user == user_id).offset(skip).limit(limit).all()

def create_favorite(db: Session, favorite: FavoriteCreate):
    db_favorite = FavoriteModel(**favorite.dict())
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
