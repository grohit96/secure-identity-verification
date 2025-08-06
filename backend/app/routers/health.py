from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter()

@router.get("/health/ping")
def ping():
    return {"message": "Backend is running successfully!"}

@router.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database is connected!"}
    except Exception as e:
        return {"error": str(e)}
