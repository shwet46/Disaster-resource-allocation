import simpy
import random
import numpy as np

# Earthquake scenario simulation
def earthquake_process(env, scenario, resources, injury_rate, aftershock_probability):
    """
    Simulates an earthquake disaster with aftershocks and varying injury rates.
    """
    yield env.timeout(1)  # Time before the earthquake hits
    
    # Main earthquake event
    print(f"Earthquake strikes at time {env.now}!")
    
    # Calculate initial damages and injuries
    injured_people = int(scenario.population * injury_rate)
    blocked_roads = random.randint(1, 5)
    
    resources["medical_supplies"]["required"] += injured_people
    resources["shelter"]["required"] += scenario.population // 2  # Half the population needs shelter
    resources["food"]["required"] += scenario.population  # All population needs food
    
    print(f"Injured: {injured_people}, Blocked Roads: {blocked_roads}")
    
    # Aftershocks
    while random.random() < aftershock_probability:
        yield env.timeout(random.randint(1, 5))  # Random delay between aftershocks
        print(f"Aftershock at time {env.now}!")
        injured_people = int(scenario.population * random.uniform(0.01, 0.05))
        blocked_roads += random.randint(0, 3)
        resources["medical_supplies"]["required"] += injured_people
        resources["shelter"]["required"] += scenario.population // 4  # More people need shelter
        print(f"Additional Injured: {injured_people}, Total Blocked Roads: {blocked_roads}")

def run_simulation(scenario):
    env = simpy.Environment()
    
    # Initialize resources needed for the earthquake scenario
    resources = {
        "medical_supplies": {"required": 0, "available": 1000},
        "shelter": {"required": 0, "available": 500},
        "food": {"required": 0, "available": 2000}
    }
    
    # Parameters specific to an earthquake
    injury_rate = 0.2  # 20% of the population is injured
    aftershock_probability = 0.3  # 30% chance of an aftershock
    
    # Start the earthquake process in the environment
    env.process(earthquake_process(env, scenario, resources, injury_rate, aftershock_probability))
    
    # Run the simulation for a total of 30 time units
    env.run(until=30)
    
    # Calculate the remaining resources
    remaining_resources = {key: max(0, val["available"] - val["required"]) for key, val in resources.items()}
    
    # Return the remaining resources and a simulated response time
    response_time = np.random.uniform(5, 15)  # Simulated response time between 5 and 15 units
    return response_time, remaining_resources
