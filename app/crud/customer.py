# app/crud/customer.py
from sqlalchemy.orm import Session
import uuid

# Impor Model ORM SQLAlchemy Customer yang BENAR (dari models)
from ..models.customer import Customer as CustomerModel

# Impor Skema Pydantic Customer (dari schemas)
from ..schemas.customer import CustomerCreate, CustomerUpdate, Customer as CustomerSchema # Impor spesifik

def get_customer(db: Session, customer_id: uuid.UUID):
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

def get_customer_by_email(db: Session, email: str):
    return db.query(CustomerModel).filter(CustomerModel.email == email).first()

def get_customer_by_uid(db: Session, firebase_uid: str):
    return db.query(CustomerModel).filter(CustomerModel.firebase_uid == firebase_uid).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CustomerModel).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: CustomerCreate): # Gunakan CustomerCreate langsung
    db_customer = CustomerModel(**customer.dict()) # Gunakan CustomerModel
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer(db: Session, customer_id: uuid.UUID, customer: CustomerUpdate): # Gunakan CustomerUpdate langsung
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if db_customer:
        for key, value in customer.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: uuid.UUID):
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer