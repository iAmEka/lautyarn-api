from fastapi import FastAPI
from .database import Base, engine
from .routers import admin, customer, rajutan, favorite, komentar

# Buat semua tabel di database (jika belum ada)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lautyarn API",
    description="API for managing Lautyarn knitting products and users.",
    version="0.1.0"
)

app.include_router(admin.router)
app.include_router(customer.router)
app.include_router(rajutan.router)
app.include_router(favorite.router)
app.include_router(komentar.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Lautyarn API!"}