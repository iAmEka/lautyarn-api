# app/routers/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

# Hapus: from .. import crud, models
# Impor Skema Admin secara spesifik
from ..schemas.admin import Admin, AdminCreate, AdminUpdate
# Impor Fungsi CRUD Admin secara spesifik
from ..crud.admin import create_admin, get_admin, get_admin_by_email, get_admins, update_admin, delete_admin
from ..database import get_db

router = APIRouter(
    prefix="/admins",
    tags=["Admins"]
)

@router.post("/", response_model=Admin)
# Saya mengubah nama fungsi menjadi create_admin_endpoint untuk menghindari ambiguitas
def create_admin_endpoint(admin: AdminCreate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_admin = get_admin_by_email(db, email=admin.email) # Gunakan get_admin_by_email langsung
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hapus "crud." di sini
    return create_admin(db=db, admin=admin) # Gunakan create_admin langsung

@router.get("/", response_model=List[Admin])
def read_admins_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    admins = get_admins(db, skip=skip, limit=limit) # Gunakan get_admins langsung
    return admins

@router.get("/{admin_id}", response_model=Admin)
def read_admin_endpoint(admin_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_admin = get_admin(db, admin_id=admin_id) # Gunakan get_admin langsung
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.put("/{admin_id}", response_model=Admin)
def update_admin_endpoint(admin_id: uuid.UUID, admin: AdminUpdate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_admin = update_admin(db, admin_id=admin_id, admin=admin) # Gunakan update_admin langsung
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.delete("/{admin_id}")
def delete_admin_endpoint(admin_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_admin = delete_admin(db, admin_id=admin_id) # Gunakan delete_admin langsung
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"message": "Admin deleted successfully"}