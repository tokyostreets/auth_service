from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError, EmailStr
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.db.models import User
from app.core.config import settings
from app.schemas.token import TokenData 

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

        subject = payload.get("sub")

        token_data = TokenData(email=subject)

        if not token_data.email:
            raise credentials_exception
        
    except (JWTError, ValidationError):
        raise credentials_exception   
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if not user:
        raise credentials_exception
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.is_active is False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user