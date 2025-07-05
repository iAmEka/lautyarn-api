from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from .. import models
from ..schemas.rajutan import Rajutan, RajutanCreate, RajutanUpdate, RajutanWithType
from ..crud.rajutan import (
    create_rajutan,
    get_rajutan,
    get_all_rajutan,
    update_rajutan,
    delete_rajutan,
)
from ..database import get_db

router = APIRouter(
    prefix="/rajutan",
    tags=["Rajutan"]
)

@router.post("/", response_model=Rajutan)
def create_rajutan_endpoint(rajutan: RajutanCreate, db: Session = Depends(get_db)):
    return create_rajutan(db=db, rajutan=rajutan)

@router.get("/", response_model=List[RajutanWithType])
def read_all_rajutan_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rajutans = get_all_rajutan(db, skip=skip, limit=limit)
    return rajutans

@router.get("/{rajutan_id}", response_model=RajutanWithType)
def read_rajutan_endpoint(rajutan_id: uuid.UUID, db: Session = Depends(get_db)):
    db_rajutan = get_rajutan(db, rajutan_id=rajutan_id)
    if db_rajutan is None:
        raise HTTPException(status_code=404, detail="Rajutan not found")
    return db_rajutan

@router.put("/{rajutan_id}", response_model=Rajutan)
def update_rajutan_endpoint(rajutan_id: uuid.UUID, rajutan: RajutanUpdate, db: Session = Depends(get_db)):
    db_rajutan = update_rajutan(db, rajutan_id=rajutan_id, rajutan=rajutan)
    if db_rajutan is None:
        raise HTTPException(status_code=404, detail="Rajutan not found")
    return db_rajutan

@router.delete("/{rajutan_id}")
def delete_rajutan_endpoint(rajutan_id: uuid.UUID, db: Session = Depends(get_db)):
    db_rajutan = delete_rajutan(db, rajutan_id=rajutan_id)
    if db_rajutan is None:
        raise HTTPException(status_code=404, detail="Rajutan not found")
    return {"message": "Rajutan deleted successfully"}
