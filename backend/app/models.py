from pydantic import BaseModel

class DisasterScenario(BaseModel):
    disaster_zone: str
    population: int
    resources: dict

class ResourceAllocationResponse(BaseModel):
    allocation: dict
    total_resources: int
    response_time: float
