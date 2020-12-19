from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_event,
    retrieve_events,
    update_event,
    delete_event,
    event_by_department,
    add_holiday,
    retrieve_holidays,
    add_notification,
    retrieve_notifications,
    add_result,
    retrieve_results)
from app.server.models.events import (
    ErrorResponseModel,
    ResponseModel,
    EventSchema,
    UpdateEventSchema)
from server.models.holidays import HolidaySchema
from server.models.notifications import NotificationSchema
from server.models.results import ResultSchema

router = APIRouter()
"""
Events
"""


@router.post("/events", response_description="Add a new event to the events list.")
async def add_event_data(event: EventSchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_event(event)
    return ResponseModel(new_event, "Event Added Succesfully.")


# Get all events
@router.get("/events", response_description="Retreive All Events")
async def get_events():
    events = await retrieve_events()
    if events:
        return ResponseModel(events, "Events data retrieved successfully")
    return ResponseModel(events, "Empty list returned")


# update event
@router.put("/{id}")
async def update_event_data(id: str, req: UpdateEventSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_event = await update_event(id, req)
    if updated_event:
        return ResponseModel(
            "Event with ID: {} name update is successful".format(id),
            "Event updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


# Delete event
@router.delete("/{id}", response_description="Event data deleted from the database")
async def delete_event_data(id: str):
    deleted_event = await delete_event(id)
    if deleted_event:
        return ResponseModel(
            "Event with ID: {} removed".format(id), "Event deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )


# Get events by department name
@router.get("/events/{name}", response_description="Department sorted events; data retrieved")
async def get_event_by_department_data(name):
    event = await event_by_department(name)
    if event:
        return ResponseModel(event, "event data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


"""
Holidays
"""


@router.post("/holidays", response_description="Add a new holiday to the holidays list.")
async def add_holiday_data(event: HolidaySchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_holiday(event)
    return ResponseModel(new_event, "Holiday Added Succesfully.")


# Get all events
@router.get("/holidays", response_description="Retreive All Holidays")
async def get_holidays():
    events = await retrieve_holidays()
    if events:
        return ResponseModel(events, "Holiday data retrieved successfully")
    return ResponseModel(events, "Empty list returned")


"""
Notifications
"""


# Add new notification
@router.post("/notifications", response_description="Add a new notification to the holidays list.")
async def add_notification_data(event: NotificationSchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_notification(event)
    return ResponseModel(new_event, "Notification Added Succesfully.")


# Get all notifications
@router.get("/notifications", response_description="Retreive All Notifications")
async def get_notification():
    events = await retrieve_notifications()
    if events:
        return ResponseModel(events, "Notification data retrieved successfully")
    return ResponseModel(events, "Empty list returned")


"""
Results
"""


# Add new result
@router.post("/results/", response_description="Add a new result to the result database.")
async def add_result_data(result: ResultSchema = Body(...)):
    result = jsonable_encoder(result)
    new_result = await add_result(result)
    return ResponseModel(new_result, "Result Added Succesfully.")


# Get all entrance results
@router.get("/results/entrance/", response_description="Retreive All Results")
async def get_result():
    results = await retrieve_results(type='Entrance')
    if results:
        return ResponseModel(results, "Results data retrieved successfully")
    return ResponseModel(results, "Empty list returned")

# Get all general results
@router.get("/results/general/", response_description="Retreive All Results")
async def get_result():
    results = await retrieve_results(type='General')
    if results:
        return ResponseModel(results, "Results data retrieved successfully")
    return ResponseModel(results, "Empty list returned")
