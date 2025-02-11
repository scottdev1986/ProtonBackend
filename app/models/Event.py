from enum import Enum

from pydantic import BaseModel, Field


class EventTypeEnum(str, Enum):
    disaster = "Disaster"
    prosperity = "Prosperity"
    attack = "Attack"
    economic_boom = "Economic Boom"
    rebellion = "Rebellion"


class EventBase(BaseModel):
    event_name: str = Field(..., max_length=255)
    event_type: EventTypeEnum
    effect: str = Field(..., description="Impact on the kingdom")
    date_occurred: str = Field(..., description="Date of event occurrence")


class EventCreate(EventBase):
    kingdom_id: int


class EventRead(EventBase):
    event_id: int
    kingdom_id: int
