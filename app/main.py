from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import user, rajutan, favorite, komentar, type_rajutan  # ✅ tambahkan type_rajutan

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lautyarn API",
    description="API for managing Lautyarn knitting products and users.",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "https://lautyarn.netlify.app",
    'https://shop-lautyarn.vercel.app',
    "https://lautyarn-website.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Daftarkan semua router
app.include_router(user.router)
app.include_router(rajutan.router)
app.include_router(favorite.router)
app.include_router(komentar.router)
app.include_router(type_rajutan.router)  # ✅ router baru ditambahkan

@app.get("/")
def read_root():
    return {"message": "Welcome to Lautyarn API!"}
