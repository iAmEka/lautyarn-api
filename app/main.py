from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware  # ✅ Tambahan penting

from .database import Base, engine
from .routers import user, rajutan, favorite, komentar  # router pengganti admin & customer

# Buat semua tabel di database (jika belum ada)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lautyarn API",
    description="API for managing Lautyarn knitting products and users.",
    version="1.0.0"
)

# ✅ Redirect otomatis HTTP -> HTTPS (hindari redirect manual yang rusak CORS)
app.add_middleware(HTTPSRedirectMiddleware)

# ✅ Konfigurasi CORS
origins = [
    "http://localhost:5173",         # Pengembangan lokal
    "https://lautyarn.netlify.app",  # Produksi (Netlify)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Untuk testing bisa ["*"], tapi hindari di produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Registrasi router yang digunakan
app.include_router(user.router)
app.include_router(rajutan.router)
app.include_router(favorite.router)
app.include_router(komentar.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Lautyarn API!"}
