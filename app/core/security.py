from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt

from app.core.config import settings


def create_access_token(subject: str | Any,
        expires_delta: Union[timedelta, None] = None) -> str:
    if expires_delta: 
        expire = datetime.now(timezone.utc) + expires_delta
    else: 
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt 

