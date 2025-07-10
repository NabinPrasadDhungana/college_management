from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app import models, auth, database
from typing import List

app = FastAPI()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not auth.authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/students", dependencies=[Depends(auth.get_current_user)])
def add_student(student: models.Student):
    student.id = len(database.students_db) + 1
    database.students_db.append(student)
    return student

@app.get("/students", response_model=List[models.Student], dependencies=[Depends(auth.get_current_user)])
def get_students():
    return database.students_db

@app.post("/courses", dependencies=[Depends(auth.get_current_user)])
def add_course(course: models.Course):
    course.id = len(database.courses_db) + 1
    database.courses_db.append(course)
    return course

@app.get("/courses", response_model=List[models.Course], dependencies=[Depends(auth.get_current_user)])
def get_courses():
    return database.courses_db
