from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from ..models.type_rajutan import TypeRajutan as TypeModel
from ..schemas.type_rajutan import (
    TypeRajutan,
    TypeRajutanCreate,
    TypeRajutanUpdate
)
from ..database import get_db

router = APIRouter(
    prefix="/type-rajutan",
    tags=["Type Rajutan"]
)

@router.post("/", response_model=TypeRajutan)
def create_type(type_data: TypeRajutanCreate, db: Session = Depends(get_db)):
    db_type = TypeModel(nama=type_data.nama)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

@router.get("/", response_model=list[TypeRajutan])
def get_all_types(db: Session = Depends(get_db)):
    return db.query(TypeModel).all()

@router.get("/{type_id}", response_model=TypeRajutan)
def get_type(type_id: UUID, db: Session = Depends(get_db)):
    tipe = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not tipe:
        raise HTTPException(status_code=404, detail="Type not found")
    return tipe

@router.put("/{type_id}", response_model=TypeRajutan)
def update_type(type_id: UUID, updated: TypeRajutanUpdate, db: Session = Depends(get_db)):
    tipe = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not tipe:
        raise HTTPException(status_code=404, detail="Type not found")
    tipe.nama = updated.nama
    db.commit()
    db.refresh(tipe)
    return tipe

@router.delete("/{type_id}")
def delete_type(type_id: UUID, db: Session = Depends(get_db)):
    tipe = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not tipe:
        raise HTTPException(status_code=404, detail="Type not found")
    db.delete(tipe)
    db.commit()
    return {"detail": "Type deleted"}
