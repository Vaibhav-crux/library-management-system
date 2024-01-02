from pydantic import BaseModel
from fastapi import Form
from typing import Optional

class BookCreate(BaseModel):
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
    book_title: str = Form(...),
    full_name: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    address: str = Form(...),
    date_of_birth: str = Form(...),
    library_card_number: str = Form(...),
    gender: str = Form(...),
    last_submit_date: str = Form(...)
    
class Student(BaseModel):
    name: str = Form(...),
    membership_start_date: str = Form(...),
    membership_expiry_date: str = Form(...)

class BookUpdate(BaseModel):
    title: Optional[str] = Form(...),
    author: Optional[str] = Form(...),
    publisher: Optional[str] = Form(...),
    publication_date: Optional[str] = Form(...),
    genre: Optional[str] = Form(...),
    cover_image: Optional[str] = Form(...),
    synopsis: Optional[str] = Form(...),
    language: Optional[str] = Form(...),
    reviews: Optional[str] = Form(...),
    status: Optional[str] = Form(...),
    book_file_link: Optional[str] = Form(...),

class UserUpdate(BaseModel):
    book_title: Optional[str] = Form(...),
    full_name: Optional[str] = Form(...),
    email: Optional[str] = Form(...),
    phone_number: Optional[str] = Form(...),
    address: Optional[str] = Form(...),
    library_card_number: Optional[str] = Form(...),
    last_submit_date: Optional[str] = Form(...)

