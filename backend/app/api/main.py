from fastapi import FastAPI
from app.db.base import Base, engine
from app.api.routers.user import router as user_router
from app.api.routers.task import router as task_router
from app.api.routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # ["http://localhost:3000"] for your frontend
    allow_credentials=True,  # Allows cookies to be sent with requests
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"message": "Hello"}


# $ uvicorn app.api.main:app --reload
