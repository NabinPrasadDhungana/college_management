from typing import List, Optional
from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    code: str
    instructor: str

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    age: int
    department: str
    email: str

class StudentCreate(StudentBase):
    course_ids: List[int] = []

class StudentOut(StudentBase):
    id: int
    courses: List[CourseOut] = []
    class Config:
        orm_mode = True