from sqlalchemy.orm import Session
from fastapi import HTTPException,Response, status
from .. import schemas, models
from ..hashing import Hash


def create(insert: schemas.User, db: Session ):
    new_user = models.User(name=insert.name,email=insert.email,password=Hash.encrypt(insert.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
 

def get_a_user(id: int, response: Response, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return user
