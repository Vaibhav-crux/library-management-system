from pydantic import BaseModel
from fastapi import Form
from typing import Optional

class BookCreate(BaseModel):
    # id: Optional[int] = Form(...),
    title: str = Form(...),
    author: str = Form(...),
    publisher: str = Form(...),
    publication_date: str = Form(...),
    genre: str = Form(...),
    cover_image: str = Form(...),
    synopsis: str = Form(...),
    language: str = Form(...),
    reviews: str = Form(...),
    status: str = Form(...),
    book_file_link: str = Form(...),

class UserDetails(BaseModel):
    # book_title: str = Form(...),
    full_name: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    address: str = Form(...),
    date_of_birth: str = Form(...),
    library_card_number: str = Form(...),
    gender: str = Form(...),
    last_submit_date: str = Form(...)
    