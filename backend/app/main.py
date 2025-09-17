from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .models import TripPlannerRequest, TripPlannerResponse, CostBreakdown
from .services.llm import build_itinerary
from .utils.cost import estimate_cost

app = FastAPI(title="AI Trip Planner ")

# Allow simple frontend prototypes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the AI Trip Planner API. Visit /docs for usage details."}

@app.post("/plan_trip", response_model=TripPlannerResponse, tags=["Trip"])
def plan_trip(payload: TripPlannerRequest):
    itinerary_txt = build_itinerary(
        payload.city,
        payload.duration,
        payload.interests,
        payload.time_pref,
        payload.budget,
    )
    costs = estimate_cost(payload.duration, payload.budget)
    return TripPlannerResponse(
        itinerary=itinerary_txt,
        cost_breakdown=CostBreakdown(**costs)
    )
