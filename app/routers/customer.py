# app/routers/customer.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

# Import schemas
from ..schemas.customer import Customer, CustomerCreate, CustomerUpdate
# Pastikan Anda mengimpor fungsi CRUD secara spesifik seperti ini:
from ..crud.customer import create_customer, get_customer, get_customer_by_email, get_customers, update_customer, delete_customer
from ..database import get_db

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=Customer)
def create_customer_endpoint(customer: CustomerCreate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_customer = get_customer_by_email(db, email=customer.email) # Panggil langsung get_customer_by_email
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hapus "crud." di sini
    return create_customer(db=db, customer=customer) # Panggil langsung create_customer

@router.get("/", response_model=List[Customer])
def read_customers_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    customers = get_customers(db, skip=skip, limit=limit) # Panggil langsung get_customers
    return customers

@router.get("/{customer_id}", response_model=Customer)
def read_customer_endpoint(customer_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_customer = get_customer(db, customer_id=customer_id) # Panggil langsung get_customer
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.put("/{customer_id}", response_model=Customer)
def update_customer_endpoint(customer_id: uuid.UUID, customer: CustomerUpdate, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_customer = update_customer(db, customer_id=customer_id, customer=customer) # Panggil langsung update_customer
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/{customer_id}")
def delete_customer_endpoint(customer_id: uuid.UUID, db: Session = Depends(get_db)):
    # Hapus "crud." di sini
    db_customer = delete_customer(db, customer_id=customer_id) # Panggil langsung delete_customer
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}