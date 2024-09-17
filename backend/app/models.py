from pydantic import BaseModel

class DisasterScenario(BaseModel):
    disaster_zone: str
    population: int
    earthquake_magnitude: float  # Added earthquake magnitude
    resources: dict

class ResourceAllocationResponse(BaseModel):
    allocation: dict
    total_resources: int
    response_time: float
    remaining_resources: dict  # Added to show remaining resources after the simulation
