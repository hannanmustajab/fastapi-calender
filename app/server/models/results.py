from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field,HttpUrl

class ResultSchema(BaseModel):
    name: str = Field(...)
    type: str = Field(...)
    url: HttpUrl = Field(...)
    timestamp: datetime = Field(default=datetime.now())
    declared : bool = Field(default=True)

    class Config:
        schema_extra = {
            "Example": {
                "name": "Holiday",
                "type": "Entrance / General",
                "timestamp": "Timestamp when the result was uploaded.",
                "url":"Enter URL if any",
                # "description":"Enter any information"
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