from fastapi import FastAPI
from app.ga_algorithm import run_ga
from app.simulation import run_simulation
from app.models import DisasterScenario, ResourceAllocationResponse
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/allocate_resources/", response_model=ResourceAllocationResponse)
async def allocate_resources(scenario: DisasterScenario):
    # Call the genetic algorithm (GA) to allocate resources
    best_allocation = run_ga(scenario)
    
    # Simulate earthquake disaster response
    response_time, remaining_resources = run_simulation(scenario)
    
    return ResourceAllocationResponse(
        allocation=best_allocation,
        total_resources=sum(best_allocation.values()),
        response_time=response_time,
        remaining_resources=remaining_resources
    )

@app.get("/")
async def root():
    return {"message": "Disaster Resource Allocation API"}
