from typing import Optional

from pydantic import BaseModel, Field

from app.models.Alignment import AlignmentEnum, Alignment


class KingdomBase(BaseModel):
    name: str = Field(..., max_length=255)
    alignment: AlignmentEnum
    treasury: int = Field(50, description="Initial Build Points (BP)")
    unrest: int = Field(0, description="Kingdom unrest level")
    size: int = Field(1, ge=1, description="Number of hexes claimed")
    economy: int = Field(0, description="Economic value of the kingdom")
    loyalty: int = Field(0, description="Loyalty of the population")
    stability: int = Field(0, description="Stability of governance")
    ruler_id: Optional[int] = Field(None, description="Ruler assigned to the kingdom")


class KingdomCreate(KingdomBase):
    """Used when a user creates a new kingdom."""

    def apply_alignment_bonuses(self):
        """Applies alignment-based bonuses to kingdom stats."""
        alignment_obj = Alignment.from_enum(self.alignment)
        self.economy += alignment_obj.economy_bonus
        self.loyalty += alignment_obj.loyalty_bonus
        self.stability += alignment_obj.stability_bonus
        return self


class KingdomRead(KingdomBase):
    """Response model for retrieving kingdom data."""

    kingdom_id: int
