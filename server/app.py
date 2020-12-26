from fastapi import FastAPI

from server.routes.routes import router as CalenderRouter
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(CalenderRouter, tags=["Calender API v1"], prefix="/api/v1/calender")

