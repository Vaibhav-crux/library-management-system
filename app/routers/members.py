from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from db.models import Student
from app.config import get_db

router = APIRouter()

__all__ = (
    "students",
)

@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.get("/students/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

@router.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()

    return db_student


@router.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()

    return db_student


@router.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: Student, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db_student.name = student_update.name

    db.commit()
    db.refresh(db_student)
    return db_student