from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.routers import addBook, loadBook, userDetails
from fastapi.middleware.cors import CORSMiddleware


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(addBook.router)
app.include_router(loadBook.router)
app.include_router(userDetails.router)
# Declarative base for models
Base = declarative_base()

# Function to create the database and tables
def create_database():
    Base.metadata.create_all(bind=engine)

# Event handler to run the function when the app starts
@app.on_event("startup")
def startup_event():
    create_database()

# Default route
@app.get("/")
async def root():
    return {"message": "Hello World"}
