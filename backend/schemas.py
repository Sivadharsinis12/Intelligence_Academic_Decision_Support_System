from pydantic import BaseModel
from datetime import datetime

class StudentCreate(BaseModel):
    name: str
    semester: int
    attendance: float
    department_id: int

class MarkCreate(BaseModel):
    student_id: int
    subject_id: int
    score: float

class SearchCreate(BaseModel):
    criteria: str
    report_type: str