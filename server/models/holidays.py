from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field,HttpUrl

class HolidaySchema(BaseModel):
    name: str = Field(...)
    start_date : datetime = Field(...)
    end_date : datetime = Field(...)
    url: Optional[HttpUrl]
    timestamp: datetime = Field(default=datetime.now())

    class Config:
        schema_extra = {
            "Example": {
                "name": "Holiday",
                "start_date": "Date Start",
                "end_date": "3.0",
                "url":"Enter URL if any"
            }
        }

class UpdateHolidaySchema(BaseModel):
    name: str = Field(...)
    start_date : datetime = Field(...)
    end_date : datetime = Field(...)
    url: Optional[HttpUrl]
    timestamp: datetime = Field(default=datetime.now())

    class Config:
        schema_extra = {
            "Example": {
                "name": "Holiday",
                "start_date": "Date Start",
                "end_date": "3.0",
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