from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

# Import schemas
from ..schemas.favorite import Favorite, FavoriteCreate

# Import CRUD function yang sudah disesuaikan ke user
from ..crud.favorite import (
    create_favorite,
    get_favorite,
    get_user_favorites,
    delete_favorite
)

from ..database import get_db

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)

# Tambah Favorite
@router.post("/", response_model=Favorite)
def create_favorite_endpoint(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return create_favorite(db=db, favorite=favorite)

# Ambil semua favorite berdasarkan user_id
@router.get("/user/{user_id}", response_model=List[Favorite])
def read_user_favorites_endpoint(user_id: uuid.UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    favorites = get_user_favorites(db, user_id=user_id, skip=skip, limit=limit)
    return favorites

# Ambil 1 favorite by ID
@router.get("/{favorite_id}", response_model=Favorite)
def read_favorite_by_id(favorite_id: uuid.UUID, db: Session = Depends(get_db)):
    favorite = get_favorite(db, favorite_id)
    if favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite

# Hapus Favorite
@router.delete("/{favorite_id}")
def delete_favorite_endpoint(favorite_id: uuid.UUID, db: Session = Depends(get_db)):
    db_favorite = delete_favorite(db, favorite_id=favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"message": "Favorite deleted successfully"}
