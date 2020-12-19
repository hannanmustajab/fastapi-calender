import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.calender

events_collection = database.get_collection("events_collection")
holidays_collection = database.get_collection("holidays_collection")
notifications_collection = database.get_collection("notifications_collection")
exams_collection = database.get_collection("exams_collection")
entrances_collection = database.get_collection("entrances_collection")
results_collection = database.get_collection("results_collection")




"""
Events related functions
"""

# helpers

def event_helper(event) -> dict:
    return {
        "id": str(event["_id"]),
        "name": event["name"],
        "description": event["description"],
        "department": event["department"],
        "start_date": event["start_date"],
        "end_date": event["end_date"],
        "url": event["url"],
        "online":event["online"],
        "faculty":event["faculty"]
    }

def faculty_department_help(event)->dict:
    # TODO
    """
    Add an event here which returns data in the following format:
        {
            "science":[maths,cs,stats],
            "arts":[economics,english]
        }
    :param event:
    :return:
    """
    return True

# Retrieve all events present in the database
async def retrieve_events():
    events = []
    async for event in events_collection.find():
        events.append(event_helper(event))
    return events


# Retrieve a student with a matching ID
async def event_by_department(department: str) -> list:
    events = []
    async for event in events_collection.find({"department": {"$regex": department, '$options': 'i'}}):
        events.append(event_helper(event))
    return events


# Add a new event into to the database
async def add_event(event_data: dict) -> dict:
    event = await events_collection.insert_one(event_data)
    new_event = await events_collection.find_one({"_id": event.inserted_id})
    return event_helper(new_event)


"""
Holidays related functions
"""
# Helper function
def holiday_helper(event)->dict:
    return {
        "id": str(event["_id"]),
        "name": event["name"],
        "start_date": event["start_date"],
        "end_date": event["end_date"],
        "url": event["url"]
    }

# Add a new holiday into to the database
async def add_holiday(holiday_data: dict) -> dict:
    holiday = await holidays_collection.insert_one(holiday_data)
    new_holiday = await holidays_collection.find_one({"_id": holiday.inserted_id})
    return holiday_helper(new_holiday)

# Retrieve all holidays present in the database
async def retrieve_holidays():
    events = []
    async for event in holidays_collection.find():
        events.append(holiday_helper(event))
    return events

"""
Notifications
"""
# Add a new holiday into to the database
async def add_notification(notification_data: dict) -> dict:
    notification = await notifications_collection.insert_one(notification_data)
    new_notification = await notifications_collection.find_one({"_id": notification.inserted_id})
    return holiday_helper(new_notification)

# Retrieve all holidays present in the database
async def retrieve_notifications():
    events = []
    async for event in notifications_collection.find():
        print(event)
        events.append(holiday_helper(event))
    return events

"""
Exam related functions
"""
# Helper Function 
def exam_helper(exam) -> dict:
    return {
        "id": str(exam["_id"]),
        "name": exam["name"],
        "faculty": exam["faculty"],
        "department": exam["department"],
        "course": exam["course"],
        "date": exam["date"],
        "course_code": exam["course_code"]
    }

# Retrieve all exams present in the database
async def retrieve_exams():
    exams = []
    async for exam in exams_collection.find():
        exams.append(exam_helper(exam))
    return exams


# Retrieve department wise exams from the database
async def exam_by_department(department: str) -> list:
    exams = []
    async for exam in exams_collection.find({"department": {"$regex": department, '$options': 'i'}}):
        exams.append(exam_helper(exam))
    return exams


# Add a new exam into to the database
async def add_exam(exam_data: dict) -> dict:
    exam = await exams_collection.insert_one(exam_data)
    new_exam = await exams_collection.find_one({"_id": exam.inserted_id})
    return exam_helper(new_exam)


"""
Entrances related functions
"""
# Helper function
def entrance_helper(entrance)->dict:
    return {
        "id": str(entrance["_id"]),
        "name": entrance["name"],
        "course": entrance["course"],
        "date": entrance["date"],
        "url": entrance["url"]
    }

# Add a new entrance into to the database
async def add_entrance(entrance_data: dict) -> dict:
    entrance = await entrances_collection.insert_one(entrance_data)
    new_entrance = await entrances_collection.find_one({"_id": entrance.inserted_id})
    return entrance_helper(new_entrance)

# Retrieve all entrances present in the database
async def retrieve_entrances():
    entrances = []
    async for entrance in entrances_collection.find():
        entrances.append(entrances_helper(entrance))
    return entrances



"""
Results
"""
def result_helper(result) -> dict:
    return {
        "id": str(result["_id"]),
        "name": result["name"],
        "url": result["url"],
        "type":result["type"],
        "declared":result["declared"]
    }
# Add a new holiday into to the database
async def add_result(result_data: dict) -> dict:
    result = await results_collection.insert_one(result_data)
    new_result = await results_collection.find_one({"_id": result.inserted_id})
    return result_helper(new_result)

# Retrieve all holidays present in the database
async def retrieve_results():
    results = []
    async for event in results_collection.find():
        results.append(result_helper(event))
    return results

