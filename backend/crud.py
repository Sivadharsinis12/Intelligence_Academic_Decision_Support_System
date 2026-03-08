from sqlalchemy.orm import Session
import models
from utils import calculate_risk

def create_student(db: Session, student):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def create_mark(db: Session, mark):
    db_mark = models.Mark(**mark.dict())
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark


def get_student_analysis(db: Session):
    students = db.query(models.Student).all()
    result = []

    for student in students:
        marks = [m.score for m in student.marks]
        avg_mark = sum(marks)/len(marks) if marks else 0
        risk = calculate_risk(avg_mark, student.attendance)

        result.append({
            "id": student.id,
            "name": student.name,
            "average_mark": avg_mark,
            "attendance": student.attendance,
            "risk_level": risk
        })

    return result


def create_search_history(db: Session, search):
    db_search = models.SearchHistory(**search.dict())
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search


def get_search_history(db: Session):
    return db.query(models.SearchHistory).all()