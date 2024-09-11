from typing  import List
from fastapi import APIRouter,  Depends, status, HTTPException, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import blog

router = APIRouter(
    prefix= '/blog',
    tags= ['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def post_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)    

@router.get('/', response_model=List[schemas.GetBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)
   

@router.get('/{id}', status_code=200, response_model=schemas.GetBlog)
def get_blog(id: int, respone: Response, db: Session = Depends(database.get_db)):
    return blog.get_one(id, respone, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def del_blog(id: int, db: Session =  Depends(database.get_db)):
    return blog.eliminate(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)