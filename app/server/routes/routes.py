from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_event,
    retrieve_events,
    event_by_department, add_holiday, retrieve_holidays, add_notification, retrieve_notifications,
    add_exam, retrieve_exams, exam_by_department, add_entrance, retrieve_entrances, add_result, retrieve_results)

from server.models.events import (
    ErrorResponseModel,
    ResponseModel,
    EventSchema
)
from server.models.holidays import HolidaySchema
from server.models.notifications import NotificationSchema
from server.models.results import ResultSchema
from server.models.exams import ExamSchema
from server.models.entrances import EntranceSchema

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


# Get events by department name
@router.get("/events/{name}", response_description="Department sorted events; data retrieved")
async def get_event_by_department_data(name):
    event = await event_by_department(name)
    if event:
        return ResponseModel(event, "event data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Event doesn't exist.")

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
EXAM
"""
# Add new exam
@router.post("/exams", response_description="Add a new exam to the exams list.")
async def add_exam_data(exam: ExamSchema = Body(...)):
    exam = jsonable_encoder(exam)
    new_exam = await add_exam(exam)
    return ResponseModel(new_exam, "Exam Added Succesfully.")

# Get all exams
@router.get("/exams", response_description="Retreive All Exams")
async def get_exams():
    exams = await retrieve_exams()
    if exams:
        return ResponseModel(exams, "Exam data retrieved successfully")
    return ResponseModel(exams, "Empty list returned")

# Get exams by department name
@router.get("/exams/{name}", response_description="Department sorted exams; data retrieved")
async def get_exam_by_department_data(name):
    exam = await exam_by_department(name)
    if exam:
        return ResponseModel(exam, "exam data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Exam doesn't exist.")


"""
ENTRANCE
"""
# Add new entrance
@router.post("/entrances", response_description="Add a new entrance to the entrances list.")
async def add_entrance_data(entrance: EntranceSchema = Body(...)):
    entrance = jsonable_encoder(entrance)
    new_entrance = await add_entrance(entrance)
    return ResponseModel(new_entrance, "Entrance Added Succesfully.")

# Get all entrances
@router.get("/entrances", response_description="Retreive All Entrances")
async def get_entrances():
    entrances = await retrieve_entrances()
    if entrances:
        return ResponseModel(entrances, "Entrances data retrieved successfully")
    return ResponseModel(entrances, "Empty list returned")


"""
Results
"""
# Add new result
@router.post("/results", response_description="Add a new result to the result database.")
async def add_result_data(result: ResultSchema = Body(...)):
    result = jsonable_encoder(result)
    new_result = await add_result(result)
    return ResponseModel(new_result, "Result Added Succesfully.")

# Get all notifications
@router.get("/results", response_description="Retreive All Results")
async def get_result():
    results = await retrieve_results()
    if results:
        return ResponseModel(results, "Results data retrieved successfully")
    return ResponseModel(results, "Empty list returned")