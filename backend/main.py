# Student Management System API


# Build a REST API to manage students.
# Features:

# Add, update, delete students

# Search by name or roll number

# JWT authentication
# What you learn:

# FastAPI basics

# CRUD operations

# Pydantic models


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Student(BaseModel):
    roll_number: int
    name: str
    age: int
    grade: str

students_db = []

@app.post("/students/", response_model=Student)
def add_student(student: Student):
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def get_students():
    return students_db

@app.get("/students/{roll_number}", response_model=Student)
def get_student(roll_number: int):
    for student in students_db:
        if student.roll_number == roll_number:
            return student
    return {"error": "Student not found"}

@app.put("/students/{roll_number}", response_model=Student)
def update_student(roll_number: int, updated_student: Student):
    for index, student in enumerate(students_db):
        if student.roll_number == roll_number:
            students_db[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{roll_number}")
def delete_student(roll_number: int):
    for index, student in enumerate(students_db):
        if student.roll_number == roll_number:
            del students_db[index]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}


@app.get("/students/search/", response_model=List[Student])
def search_students(name: Optional[str] = None, roll_number: Optional[int] = None):
    results = [] 
    for student in students_db:
        if (name and name.lower() in student.name.lower()) or (roll_number and student.roll_number == roll_number):
            results.append(student)
    return results

# Note: JWT authentication is not implemented in this code snippet for simplicity.

# In a real-world application, you would use libraries like FastAPI JWT Auth or PyJWT to implement authentication.

# To run the application, use the command:

# uvicorn main:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

# Student Management System API #