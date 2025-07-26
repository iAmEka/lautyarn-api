from sqlalchemy.orm import Session
from ..models.item_cart import ItemCart
from ..schemas.item_cart import ItemCartUpdate
from uuid import UUID

def update_item_cart(db: Session, item_cart_id: UUID, item_update: ItemCartUpdate):
    item = db.query(ItemCart).filter(ItemCart.id == item_cart_id).first()
    if item:
        for key, value in item_update.dict(exclude_unset=True).items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item

def delete_item_cart(db: Session, item_cart_id: UUID):
    item = db.query(ItemCart).filter(ItemCart.id == item_cart_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
