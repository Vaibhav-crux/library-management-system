# library-management-system

# Function Documentation: add_book

This function adds a new book to the database.

## Arguments

- **payload (BookCreate):** The book data to add.
- **db (Session):** The database session.

## Returns

- **dict:** A message indicating whether the book was added or not.

## Raises

- **HTTPException:** If there was an error adding the book.

## Usage

```python
async def add_book(payload: BookCreate, db: Session = Depends(get_db)):
    try:
        # Check if the book already exists
        existing_book = db.query(Book).filter(
            Book.title == payload.title,
            Book.author == payload.author
        ).first()

        if existing_book:
            return {"message": "The book is already added"}

        # Add the book to the database
        db_book = Book(**payload.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return {"message": "Book added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
