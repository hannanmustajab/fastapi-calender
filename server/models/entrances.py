from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl

class EntranceSchema(BaseModel):
    name: str = Field(...)
    course: str = Field(...)
    date : datetime = Field(...)
    url: Optional[HttpUrl]

    class Config:
        schema_extra = {
            "Example": {
                "name": "Entrance Name",
                "course": "Btech",
                "date": "Entrance Date",
                "url":"Enter URL if any"
            }
        }

class UpdateEntranceSchema(BaseModel):
    name: str = Field(...)
    course: str = Field(...)
    date : datetime = Field(...)
    url: Optional[HttpUrl]

    class Config:
        schema_extra = {
            "Example": {
                "name": "Entrance Name",
                "course": "Btech",
                "date": "Entrance Date",
                "url":"Enter URL if any"
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