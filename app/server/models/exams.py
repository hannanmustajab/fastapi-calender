from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class ExamSchema(BaseModel):
    name: str = Field(...)
    department: str = Field(...)
    faculty: str = Field(...)
    course: str = Field(...)
    date : datetime = Field(...)
    course_code : str = Field(...)


    class Config:
        schema_extra = {
            "Example": {
                "name": "Exam",
                "faculty": "RK Goyal",
                "department": "Computer Science",
                "course": "BCA",
                "date": "Exam Date",
                "course_code": "mmb252"
                
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}