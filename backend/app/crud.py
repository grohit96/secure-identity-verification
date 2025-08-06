from sqlalchemy.orm import Session
from app import models
from app.schemas import UserCreate
from app.security import get_password_hash   # (you'll add later for hashing)

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
