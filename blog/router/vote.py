from fastapi import APIRouter,  Depends, status, HTTPException, Response
from .. import database, models, schemas, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/vote',
    tags=['Votes'] 
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.blog_id == vote.blog_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User {current_user.id } has voted already on blog {vote.blog_id}')
        new_vote = models.Vote(blog_id = vote.blog_id,  user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {'message': 'Vote added successfully'}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vote does not exist')
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {'message': 'Vote deleted successfully'}
