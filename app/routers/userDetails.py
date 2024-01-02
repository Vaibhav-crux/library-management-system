from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import Book, User
from app.config import get_db
from app.db.schemas import UserDetails


router = APIRouter()

__all__ = (
    "submit_details",
    "get_book_title"
)

@router.post("/submit_details", response_model=dict)
async def submit_details(payload: UserDetails, db: Session = Depends(get_db)):
    try:

        db_user = User(**payload.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "Details submitted successfully"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/get_book_title/{book_id}", response_model=dict)
def get_book_title(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        return {"book_title": book.title}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
