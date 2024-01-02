from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import Book
from app.config import get_db

router = APIRouter()

__all__ = (
    "get_all_book",
    "delete_book"
)

@router.get("/get_all_book", response_model=dict)
def get_data(db: Session = Depends(get_db)):
    try:
        books = db.query(Book).all()
        return {"data": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/delete_book/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")