from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import Book
from app.db.schemas import BookCreate
from app.config import get_db
from datetime import datetime
from fastapi.responses import JSONResponse

router = APIRouter()

__all__ = (
    "add_book"
)


@router.post("/add_book", response_model=dict)
async def add_book(payload: BookCreate, db: Session = Depends(get_db)):
    try:

        existing_book = db.query(Book).filter(
            Book.title == payload.title,
            Book.author == payload.author
        ).first()

        if existing_book:
            return {"message": "The book is already added"}
        
        db_book = Book(**payload.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return {"message": "Book added successfully"}
    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=500)
