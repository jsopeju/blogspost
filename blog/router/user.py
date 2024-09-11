from typing  import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import user

router = APIRouter(
    prefix= '/user',
    tags= ['Users']
)


@router.post('/')
def create_user(insert: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(insert, db)
    

@router.get('/', response_model=List[schemas.GetUser])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/{id}', status_code=200, response_model=schemas.GetUser)
def get_user(id, respone: Response, db: Session = Depends(database.get_db)):
    return user.get_a_user(id, respone, db)