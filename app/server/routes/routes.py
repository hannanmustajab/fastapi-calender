from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_event,
    retrieve_events
)
from app.server.models.events import (
    ErrorResponseModel,
    ResponseModel,
    EventSchema
)


router = APIRouter()

@router.post("/events", response_description="Add a new event to the events list.")
async def add_event_data(event: EventSchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_event(event)
    return ResponseModel(new_event, "Event Added Succesfully.")

#Get all events

@router.get("/events", response_description="Retreive All Events")
async def get_events():
    events = await retrieve_events()
    if events:
        return ResponseModel(events, "Events data retrieved successfully")
    return ResponseModel(events, "Empty list returned")