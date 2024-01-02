from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    author: Mapped[str] = mapped_column(String)
    publisher: Mapped[str] = mapped_column(String)
    publication_date: Mapped[str] = mapped_column(String)
    genre: Mapped[str] = mapped_column(String)
    cover_image: Mapped[str] = mapped_column(String)
    synopsis: Mapped[str] = mapped_column(String)
    language: Mapped[str] = mapped_column(String)
    reviews: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    book_file_link: Mapped[str] = mapped_column(String)

class User(Base):
    __tablename__ = 'book_details'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # book_title: Mapped[str] = mapped_column(String, index=True)
    full_name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    date_of_birth: Mapped[str] = mapped_column(String)
    library_card_number: Mapped[str] = mapped_column(String)
    gender: Mapped[str] = mapped_column(String)
    last_submit_date: Mapped[str] = mapped_column(String)

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    membership_start_date: Mapped[str] = mapped_column(String)
    membership_expiry_date: Mapped[str] = mapped_column(String)