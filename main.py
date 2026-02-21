from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/dashboard")
def dashboard():
    return FileResponse("dashboard.html")

@app.get("/analytics")
def analytics():
    return FileResponse("analytics.html")

@app.get("/history")
def history():
    return FileResponse("history.html")
# KPI Data
@app.get("/api/kpi")
def get_kpi():
    return {
        "average_performance": 78.4,
        "attendance": 92,
        "attendance_change": -0.5,
        "at_risk": 14,
        "course_outcome": 85,
        "outcome_variance": -1.2
    }

# Chart Data
@app.get("/api/performance-trend")
def performance_trend():
    return {
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "values": [65, 74, 70, 85, 80, 92]
    }

# Table Data
@app.get("/api/student-inquiries")
def student_inquiries():
    return [
        {
            "id": "ST-8821",
            "department": "Computer Science",
            "status": "Stable",
            "prediction": "94% Success"
        },
        {
            "id": "ST-7734",
            "department": "Mechanical Eng.",
            "status": "Needs Attention",
            "prediction": "62% Success"
        },
        {
            "id": "ST-9102",
            "department": "Bio-Chemistry",
            "status": "At Risk",
            "prediction": "45% Success"
        }
    ]@app.get("/api/analytics/students")
def get_students():
    return [
        {"initials":"AM","name":"Arjun Mehta","marks":88,"attendance":92,"risk":"Low"},
        {"initials":"SK","name":"Sara Khan","marks":42,"attendance":65,"risk":"High"},
        {"initials":"LD","name":"Leo Das","marks":76,"attendance":88,"risk":"Medium"},
        {"initials":"RP","name":"Rohan Prasad","marks":64,"attendance":74,"risk":"Medium"},
    ]

@app.get("/api/analytics/difficulty")
def get_difficulty():
    return [
        {"subject":"Advanced Mathematics","value":85},
        {"subject":"Data Structures","value":62},
        {"subject":"Web Development","value":34},
    ]@app.get("/api/history")
def get_history():
    return [
        {
            "date": "Oct 24, 2023",
            "time": "10:15 AM",
            "criteria": ["Enrollment", "Fall 2024"],
            "type": "Enrollment Projection"
        },
        {
            "date": "Oct 22, 2023",
            "time": "02:30 PM",
            "criteria": ["Budget", "Faculty Salary"],
            "type": "Budget Impact"
        },
        {
            "date": "Oct 20, 2023",
            "time": "09:12 AM",
            "criteria": ["Graduation", "Class 2023"],
            "type": "Student Success"
        }
    ]