from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,Response, status

def get_all(db: Session):
     blogs = db.query(models.Blog).all()
     return blogs

def get_one(id: int, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return blog

def create(request: schemas.Blog, db: Session):
     new_blog = models.Blog(title=request.title, content=request.content, published=request.published, user_id=2)
     db.add(new_blog)
     db.commit()
     db.refresh(new_blog)
     return new_blog

def eliminate(id: int, db: Session):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist")
     blog.delete(synchronize_session=False)
    
     db.commit()

     return {'detail': 'Blog successfully deleted'}

def update(id: int, request: schemas.Blog, db: Session):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist")
     blog.update(request)

     db.commit()

     return {'detail': 'Blog successfully updated'}

