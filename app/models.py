from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str

class Student(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    department: str

class Course(BaseModel):
    id: Optional[int] = None
    title: str
    code: str
    instructor: str
