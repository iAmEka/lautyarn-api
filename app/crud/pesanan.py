from sqlalchemy.orm import Session
from uuid import uuid4
from ..models.pesanan import Pesanan
from ..models.detail_pesanan import DetailPesanan
from ..schemas import pesanan as pesanan_schemas

def create_pesanan(db: Session, pesanan_data: pesanan_schemas.PesananCreate):
    pesanan_obj = Pesanan(id=uuid4(), user_id=pesanan_data.user_id)
    db.add(pesanan_obj)
    db.flush()  # biar pesanan_obj.id bisa dipakai di detail

    for item in pesanan_data.detail:
        detail = DetailPesanan(
            id=uuid4(),
            pesanan_id=pesanan_obj.id,
            rajutan_id=item.rajutan_id,
            quantity=item.quantity,
        )
        db.add(detail)

    db.commit()
    db.refresh(pesanan_obj)
    return pesanan_obj

def get_all_pesanan(db: Session):
    return db.query(Pesanan).all()
