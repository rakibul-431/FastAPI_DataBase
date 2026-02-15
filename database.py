from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MYSQL_USER='root'
MYSQL_PASSWORD='Rakibul43@11'
MYSQL_HOST='localhost'
MYSQL_PORT='3306'
DATABASE_NAME='fastapi'

DATABASE_URL=f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DATABASE_NAME}'

##Connection with database
engine=create_engine(DATABASE_URL)

##Creating a session
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

##Base 
Base=declarative_base()

