from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic.types import conint

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str



class GetUser(User):
    class Config():
        from_attribute = True


class Blog(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool]
    user_id: int
    owner: GetUser

class GetBlog(Blog):
    class Config():
        from_attribute = True

class Signin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class Vote(BaseModel):
    blog_id: int
    dir: conint(le=1)

