from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field,HttpUrl

class EventSchema(BaseModel):
    name: str = Field(...)
    faculty: str = Field(...)
    department: str = Field(...)
    description: str = Field(...,max_length=300)
    start_date : datetime = Field(...)
    end_date : datetime = Field(...)
    url: Optional[HttpUrl]
    online: bool = Field(...)
    timestamp: datetime = Field(default=datetime.now())


    class Config:
        schema_extra = {
            "Example": {
                "name": "Example Event",
                "department": "Computer Science",
                "description": "Dsknkjskm  hjdsbhjsbh",
                "start_date": "Date Start",
                "end_date": "3.0",
                "url":"Enter URL if any",
                "online":False          #Default
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