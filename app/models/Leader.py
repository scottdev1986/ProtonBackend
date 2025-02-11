from enum import Enum

from pydantic import BaseModel, Field


class LeaderRoleEnum(str, Enum):
    ruler = "Ruler"
    high_priest = "High Priest"
    treasurer = "Treasurer"
    general = "General"
    councilor = "Councilor"
    spymaster = "Spymaster"
    magister = "Magister"
    marshal = "Marshal"
    royal_enforcer = "Royal Enforcer"
    grand_diplomat = "Grand Diplomat"
    viceroy = "Viceroy"
    warden = "Warden"


class Leader(BaseModel):
    name: str = Field(..., max_length=255)
    role: LeaderRoleEnum
    ability_bonus: int = Field(
        ..., description="Ability bonus applied to kingdom stats"
    )


class LeaderCreate(Leader):
    kingdom_id: int


class LeaderRead(Leader):
    leader_id: int
    kingdom_id: int
