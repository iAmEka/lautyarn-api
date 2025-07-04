# app/routers/favorite.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

# Import schemas
from ..schemas.favorite import Favorite, FavoriteCreate
# Pastikan Anda mengimpor fungsi CRUD secara spesifik seperti ini:
from ..crud.favorite import create_favorite, get_favorite, get_customer_favorites, delete_favorite
from ..database import get_db

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)

@router.post("/", response_model=Favorite)
# Saya mengubah nama fungsi menjadi create_favorite_endpoint untuk kejelasan, tapi tidak wajib.
def create_favorite_endpoint(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    return create_favorite(db=db, favorite=favorite) # Panggil langsung create_favorite

@router.get("/customer/{customer_id}", response_model=List[Favorite])
def read_customer_favorites_endpoint(customer_id: uuid.UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    favorites = get_customer_favorites(db, customer_id=customer_id, skip=skip, limit=limit) # Panggil langsung get_customer_favorites
    return favorites

@router.delete("/{favorite_id}")
def delete_favorite_endpoint(favorite_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_favorite = delete_favorite(db, favorite_id=favorite_id) # Panggil langsung delete_favorite
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"message": "Favorite deleted successfully"}