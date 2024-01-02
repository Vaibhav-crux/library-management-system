from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.db.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()
Base.metadata.create_all(bind=engine, checkfirst=True)  # Add this line
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()