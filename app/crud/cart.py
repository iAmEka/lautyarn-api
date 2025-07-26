from sqlalchemy.orm import Session
from uuid import uuid4
from ..models.cart import Cart
from ..models.item_cart import ItemCart
from ..schemas import cart as cart_schemas

def create_cart(db: Session, cart_data: cart_schemas.CartCreate):
    cart_obj = Cart(id=uuid4(), user_id=cart_data.user_id)
    db.add(cart_obj)
    db.flush()  # supaya id bisa dipakai

    for item in cart_data.items:
        item_obj = ItemCart(
            id=uuid4(),
            cart_id=cart_obj.id,
            rajutan_id=item.rajutan_id,
            quantity=item.quantity,
            price_at_added=item.price_at_added,
            status=item.status,
        )
        db.add(item_obj)

    db.commit()
    db.refresh(cart_obj)
    return cart_obj

def get_cart(db: Session, cart_id):
    return db.query(Cart).filter(Cart.id == cart_id).first()

def get_cart_by_user(db: Session, user_id):
    return db.query(Cart).filter(Cart.user_id == user_id).all()
