from sqlalchemy.orm import Session
from ..models.detail_pesanan import DetailPesanan

def update_quantity(db: Session, detail_id, new_quantity):
    detail = db.query(DetailPesanan).filter(DetailPesanan.id == detail_id).first()
    if detail:
        detail.quantity = new_quantity
        db.commit()
        db.refresh(detail)
    return detail
