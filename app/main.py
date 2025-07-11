from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import auth, database, schemas, crud, models

from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not auth.authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/students", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.create_student(db, student)

@app.get("/students", response_model=list[schemas.StudentOut])
def read_students(db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.get_students(db)

@app.post("/courses", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.create_course(db, course)

@app.get("/courses", response_model=list[schemas.CourseOut])
def read_courses(db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.get_courses(db)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    deleted = crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": f"Student with ID {student_id} deleted"}

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    deleted = crud.delete_course(db, course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"detail": f"Course with ID {course_id} deleted"}
