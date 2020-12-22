from fastapi import FastAPI

from server.routes.routes import router as CalenderRouter

app = FastAPI()

app.include_router(CalenderRouter, tags=["Calender API v1"], prefix="/api/v1/calender")

