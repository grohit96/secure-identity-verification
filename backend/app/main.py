from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health  # keep as is if filename is verificaton.py

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