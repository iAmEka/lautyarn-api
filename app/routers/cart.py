from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from ..database import get_db
from ..schemas.cart import CartCreate, CartResponse
from ..crud.cart import create_cart, get_cart, get_cart_by_user
from ..schemas.item_cart import ItemCartUpdate
from ..crud.item_cart import update_item_cart, delete_item_cart

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartResponse)
def create_cart_endpoint(cart: CartCreate, db: Session = Depends(get_db)):
    return create_cart(db, cart)

@router.get("/user/{user_id}", response_model=List[CartResponse])
def get_user_carts(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_cart_by_user(db, user_id)

@router.get("/{cart_id}", response_model=CartResponse)
def get_cart_endpoint(cart_id: uuid.UUID, db: Session = Depends(get_db)):
    cart = get_cart(db, cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.put("/item/{item_id}", response_model=ItemCartUpdate)
def update_item_endpoint(item_id: uuid.UUID, item_update: ItemCartUpdate, db: Session = Depends(get_db)):
    updated_item = update_item_cart(db, item_id, item_update)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/item/{item_id}")
def delete_item_endpoint(item_id: uuid.UUID, db: Session = Depends(get_db)):
    deleted_item = delete_item_cart(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
