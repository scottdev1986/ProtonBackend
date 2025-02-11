from enum import Enum

from pydantic import BaseModel, Field


class SettlementSizeEnum(str, Enum):
    thorp = "Thorp"
    hamlet = "Hamlet"
    village = "Village"
    small_town = "Small Town"
    large_town = "Large Town"
    small_city = "Small City"
    large_city = "Large City"
    metropolis = "Metropolis"


class SettlementBase(BaseModel):
    name: str = Field(..., max_length=255)
    population: int = Field(100, ge=0, description="Settlement population")
    size: SettlementSizeEnum

    @classmethod
    def calculate_settlement_size(cls, population: int):
        """Determine settlement size category based on population."""
        size_map = [
            (21, "Thorp"),
            (60, "Hamlet"),
            (200, "Village"),
            (2000, "Small Town"),
            (5000, "Large Town"),
            (10000, "Small City"),
            (25000, "Large City"),
            (9999999, "Metropolis"),
        ]
        for pop_limit, size in size_map:
            if population <= pop_limit:
                return SettlementSizeEnum(size.lower().replace(" ", "_"))


class SettlementCreate(SettlementBase):
    kingdom_id: int


class SettlementRead(SettlementBase):
    settlement_id: int
    kingdom_id: int
