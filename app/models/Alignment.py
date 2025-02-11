from pydantic import BaseModel, Field
from enum import Enum


class AlignmentEnum(str, Enum):
    lawful_good = "Lawful Good"
    neutral_good = "Neutral Good"
    chaotic_good = "Chaotic Good"
    lawful_neutral = "Lawful Neutral"
    neutral = "Neutral"
    chaotic_neutral = "Chaotic Neutral"
    lawful_evil = "Lawful Evil"
    neutral_evil = "Neutral Evil"
    chaotic_evil = "Chaotic Evil"


class Alignment(BaseModel):
    name: AlignmentEnum
    economy_bonus: int = Field(0, description="Bonus to Economy")
    loyalty_bonus: int = Field(0, description="Bonus to Loyalty")
    stability_bonus: int = Field(0, description="Bonus to Stability")

    @classmethod
    def from_enum(cls, alignment: AlignmentEnum):
        bonuses = {
            "Lawful Good": {
                "economy_bonus": 2,
                "loyalty_bonus": 2,
                "stability_bonus": 0,
            },
            "Neutral Good": {
                "economy_bonus": 0,
                "loyalty_bonus": 2,
                "stability_bonus": 0,
            },
            "Chaotic Good": {
                "economy_bonus": 0,
                "loyalty_bonus": 2,
                "stability_bonus": 0,
            },
            "Lawful Neutral": {
                "economy_bonus": 2,
                "loyalty_bonus": 0,
                "stability_bonus": 0,
            },
            "Neutral": {"economy_bonus": 0, "loyalty_bonus": 0, "stability_bonus": 4},
            "Chaotic Neutral": {
                "economy_bonus": 0,
                "loyalty_bonus": 2,
                "stability_bonus": 0,
            },
            "Lawful Evil": {
                "economy_bonus": 2,
                "loyalty_bonus": 0,
                "stability_bonus": 0,
            },
            "Neutral Evil": {
                "economy_bonus": 2,
                "loyalty_bonus": 0,
                "stability_bonus": 0,
            },
            "Chaotic Evil": {
                "economy_bonus": 0,
                "loyalty_bonus": 2,
                "stability_bonus": 0,
            },
        }
        return cls(name=alignment, **bonuses[alignment])
