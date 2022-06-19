from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, oauth2
from ..database import get_db
from ..repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)


@router.get('', response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def save_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    return blog.create_blog(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, )
def get_single_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_single_blog(id, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    return blog.update_blog(id, request, db)
