from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_event,
    retrieve_events,

    update_event,
    delete_event,
    event_by_department,
    add_holiday,
    retrieve_holidays,
    update_holiday,
    delete_holiday,
    add_notification,
    retrieve_notifications,
    update_notification,
    delete_notification,
    add_exam,
    retrieve_exams,
    update_exam,
    delete_exam,
    exam_by_department,
    add_entrance,
    retrieve_entrances,
    update_entrance,
    delete_entrance,
    add_result,
    retrieve_results,
    update_result,
    delete_result)

from server.models.events import (
    ErrorResponseModel,
    ResponseModel,
    EventSchema,
    UpdateEventSchema)
from server.models.holidays import (
    ErrorResponseModel,
    ResponseModel,
    HolidaySchema,
    UpdateHolidaySchema)

from server.models.notifications import (
    ErrorResponseModel,
    ResponseModel,
    NotificationSchema,
    UpdateNotificationSchema)
from server.models.results import (
    ErrorResponseModel,
    ResponseModel,
    ResultSchema,
    UpdateResultSchema)
from server.models.exams import (
    ErrorResponseModel,
    ResponseModel,
    ExamSchema,
    UpdateExamSchema)

from server.models.entrances import (
    ErrorResponseModel,
    ResponseModel,
    EntranceSchema,
    UpdateEntranceSchema)
   

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
    return ErrorResponseModel("An error occurred.", 404, "Event doesn't exist.")


"""
Holidays
"""


@router.post("/holidays", response_description="Add a new holiday to the holidays list.")
async def add_holiday_data(event: HolidaySchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_holiday(event)
    return ResponseModel(new_event, "Holiday Added Succesfully.")


# Get all holidays
@router.get("/holidays", response_description="Retreive All Holidays")
async def get_holidays():
    events = await retrieve_holidays()
    if events:
        return ResponseModel(events, "Holiday data retrieved successfully")
    return ResponseModel(events, "Empty list returned")

# update holidays
@router.put("/holidays/{id}")
async def update_holiday_data(id: str, req: UpdateHolidaySchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_holiday = await update_holiday(id, req)
    if updated_holiday:
        return ResponseModel(
            "Holiday with ID: {} name update is successful".format(id),
            "Holiday updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the holiday data.",
    )


# Delete holiday
@router.delete("/holidays/{id}", response_description="Holiday data deleted from the database")
async def delete_holiday_data(id: str):
    deleted_holiday = await delete_holiday(id)
    if deleted_holiday:
        return ResponseModel(
            "Holiday  with ID: {} removed".format(id), "Event deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Holiday with id {0} doesn't exist".format(id)
    )




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

# update notification
@router.put("/notifications/{id}")
async def update_notification_data(id: str, req: UpdateNotificationSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_notification = await update_notification(id, req)
    if updated_notification:
        return ResponseModel(
            "Notification with ID: {} name update is successful".format(id),
            "Notification updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the notification data.",
    )


# Delete event
@router.delete("/notifications/{id}", response_description="Notification data deleted from the database")
async def delete_notification_data(id: str):
    deleted_notification = await delete_notification(id)
    if deleted_notification:
        return ResponseModel(
            "Notification with ID: {} removed".format(id), "Notification deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Notification with id {0} doesn't exist".format(id)
    )





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


# update exam
@router.put("/exams/{id}")
async def update_exam_data(id: str, req: UpdateExamSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_exam = await update_exam(id, req)
    if updated_exam:
        return ResponseModel(
            "Exam with ID: {} name update is successful".format(id),
            "Exam updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the exam data.",
    )


# # Delete exam
@router.delete("/exams/{id}", response_description="Exam data deleted from the database")
async def delete_exam_data(id: str):
    deleted_exam = await delete_exam(id)
    if deleted_exam:
        return ResponseModel(
            "Exam with ID: {} removed".format(id), "Exam deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Exam with id {0} doesn't exist".format(id)
    )


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

# update entrance
@router.put("/entrances/{id}")
async def update_entrance_data(id: str, req: UpdateEntranceSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_entrance = await update_entrance(id, req)
    if updated_entrance:
        return ResponseModel(
            "Entrance with ID: {} name update is successful".format(id),
            "Entrance updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the entrance data.",
    )


# Delete entrance
@router.delete("/entrances/{id}", response_description="Entrance data deleted from the database")
async def delete_entrance_data(id: str):
    deleted_entrance = await delete_entrance(id)
    if deleted_entrance:
        return ResponseModel(
            "Entrance with ID: {} removed".format(id), "Entrance deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Entrance with id {0} doesn't exist".format(id)
    )



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


# update entrance results
@router.put("/results/{id}")
async def update_result_data(id: str, req: UpdateResultSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    print(req)
    if req['type'] == 'Entrance':
        updated_entrance_result = await update_result(id, req)
        if updated_entrance_result:
            return ResponseModel(
                "Entrance Result with ID: {} name update is successful".format(id),
                "Entrance Result updated successfully",
            )
    else:
        updated_general_result = await update_result(id, req)
        if updated_general_result:
            return ResponseModel(
                "Entrance Result with ID: {} name update is successful".format(id),
                "Entrance Result updated successfully",
            )

    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the entrance/general result data.",
    )


# Delete result
@router.delete("/results/{id}", response_description="Results data deleted from the database")
async def delete_result_data(id: str):
    deleted_result = await delete_result(id)
    if deleted_result:
        return ResponseModel(
            "Result with ID: {} removed".format(id), "Result deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Result with id {0} doesn't exist".format(id)
    )