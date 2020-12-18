import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.calender

events_collection = database.get_collection("events_collection")


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
        # "online":event["online"],
        # "tags":event["tags"],
        # "faculty":event["faculty"]

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


# Retrieve all students present in the database
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
