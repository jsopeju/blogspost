from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import  models
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .router import blog, user, authentication, vote
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credential=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(vote.router)



#def get_db():
 #   db = SessionLocal()
    
  #  try:
   #     yield db

    #finally:
     #   db.close()


#@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
#def post_blog(request: schemas.Blog, db: Session = Depends(get_db)):
 #   new_blog = models.Blog(title=request.title, content=request.content, published=request.published, user_id=20)
  #  db.add(new_blog)
   # db.commit()
   # db.refresh(new_blog)
    #return new_blog


#@app.get('/blog', response_model=List[schemas.GetBlog], tags=['Blogs'])
#def get_blogs(db: Session = Depends(get_db)):
 #   blogs = db.query(models.Blog).all()
  #  return blogs


#@app.get('/blog/{id}', status_code=200, response_model=schemas.GetBlog, tags=['Blogs'])
#def get_blog(id, respone: Response, db: Session = Depends(get_db)):
 #   blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  #  if not blog:
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    #return blog



#@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
#def del_blog(id, db: Session = Depends(get_db)):
 #   blog = db.query(models.Blog).filter(models.Blog.id == id)
  #  if not blog.first():
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist")
    #blog.delete(synchronize_session=False)
    
    #db.commit()

    #return {'detail': 'Blog successfully deleted'}


#@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
#def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
 #   blog = db.query(models.Blog).filter(models.Blog.id == id)
  #  if not blog.first():
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesn't exist")
    #blog.update(request)

    #db.commit()

    #return {'detail': 'Blog successfully updated'}




#@app.post('/user', tags=['Users'])
#def create_user(insert: schemas.User, db: Session = Depends(get_db)):
 #   new_user = models.User(name=insert.name,email=insert.email,password=Hash.encrypt(insert.password))
  #  db.add(new_user)
   # db.commit()
   # db.refresh(new_user)

    #return new_user


#@app.get('/user', response_model=List[schemas.GetUser], tags=['Users'])
#def get_users(db: Session = Depends(get_db)):
 #   users = db.query(models.User).all()
  #  return users


#@app.get('/user/{id}', status_code=200, response_model=schemas.GetUser, tags=['Users'])
#def get_user(id, respone: Response, db: Session = Depends(get_db)):
 #   user = db.query(models.User).filter(models.User.id == id).first()
  #  if not user:
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    #return user
