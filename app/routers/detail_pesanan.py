from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..crud.detail_pesanan import update_quantity

router = APIRouter(prefix="/detail-pesanan", tags=["Detail Pesanan"])

@router.put("/{detail_id}")
def update_detail(detail_id: str, quantity: int, db: Session = Depends(get_db)):
    return update_quantity(db, detail_id, quantity)
