#main
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Backend.database import engine, Base, SessionLocal
from Backend import models # loads observation models
from Backend.schemas import ObservationCreate

app = FastAPI()
Base.metadata.create_all(bind=engine) # creates the necessary tables in the database from what ive made in models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")

def home():
    return {"message": "Welcome to Fast Track!"}

@app.post("/observations")
def create_observation(
        observation: ObservationCreate,
        db: Session = Depends(get_db)
):
    new_observation = models.Observation(
        title=observation.title,
        description=observation.description,
        location=observation.location
    )

    db.add(new_observation)
    db.commit()
    db.commit()
    db.refresh(new_observation)
    return new_observation


