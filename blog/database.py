from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATEBASE_URL = 'sqlite:///./post.db'


engine = create_engine(SQLALCHEMY_DATEBASE_URL, connect_args={'check_same_thread': False})


SessionLocal = sessionmaker(bind=engine, autocommit= False, autoflush= False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    
    try:
        yield db

    finally:
        db.close()
