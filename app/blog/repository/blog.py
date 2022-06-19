from sqlalchemy.orm import Session
from fastapi import status, HTTPException

from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_single_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    else:
        return blog


def delete_blog(id, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Blog Deleted Successfully!'}


def update_blog(id, request: schemas.Blog, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")

    blog.update(request)
    db.commit()
    return {'detail': 'Blog Updated Successfully!'}
