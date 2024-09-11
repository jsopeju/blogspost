from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from . import JWT_Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='SIGNIN')


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    ) 

    return JWT_Token.verify_Jwt_token(data, credentials_exception)