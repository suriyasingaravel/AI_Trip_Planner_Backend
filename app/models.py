from pydantic import BaseModel, Field
from typing import Optional, Dict

class TripPlannerRequest(BaseModel):
    city: str = Field(..., example="Jaipur")
    duration: int = Field(..., gt=0, example=4, description="Trip length in days")
    interests: str = Field(..., example="heritage, street food")
    time_pref: str = Field(..., example="full day")
    budget: Optional[float] = Field(None, example=30000)

class CostBreakdown(BaseModel):
    accommodation: float
    food: float
    transport: float
    entrance_fees: float
    misc: float
    total: float

class TripPlannerResponse(BaseModel):
    itinerary: str
    cost_breakdown: CostBreakdown
