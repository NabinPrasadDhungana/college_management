from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        age=student.age,
        department=student.department,
        email=student.email
    )
    db_student.courses = db.query(models.Course).filter(models.Course.id.in_(student.course_ids)).all()
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student

def get_students(db: Session):
    return db.query(models.Student).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        return None
    db.delete(course)
    db.commit()
    return course

def get_courses(db: Session):
    return db.query(models.Course).all()

def update_student(db: Session, student_id: int, updated_student: schemas.StudentCreate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    student.name = updated_student.name
    student.age = updated_student.age
    student.department = updated_student.department
    student.email = updated_student.email
    # Update courses relation
    student.courses = db.query(models.Course).filter(models.Course.id.in_(updated_student.course_ids)).all()
    db.commit()
    db.refresh(student)
    return student

def update_course(db: Session, course_id: int, updated_course: schemas.CourseCreate):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        return None
    course.title = updated_course.title
    course.code = updated_course.code
    course.instructor = updated_course.instructor
    db.commit()
    db.refresh(course)
    return course

