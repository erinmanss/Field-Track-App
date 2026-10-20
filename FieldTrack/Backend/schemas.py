from pydantic import BaseModel

class ObservationCreate(BaseModel):
    title: str
    description: str | None = None
    location: str | None = None
#info user can send when creating observation