from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, token
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: models.User = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect Pasword")

        # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
