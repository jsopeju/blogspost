from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship



class Blog(Base):

    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("Users.id"))

    owner = relationship("User", back_populates="blogs")



class User(Base):


    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(Boolean)
    
    blogs = relationship("Blog", back_populates="owner")


class Vote(Base):

    __tablename__ = 'Votes'
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)