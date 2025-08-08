from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health  # keep as is if filename is verificaton.py
from app.routers import users 
from app.routers import auth

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(auth.router)