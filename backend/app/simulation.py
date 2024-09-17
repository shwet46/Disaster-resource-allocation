import simpy
import numpy as np

def simulate_disaster(env, scenario):
    resources = scenario['resources']
    while True:
        for resource in resources:
            resource['available'] -= np.random.randint(0, 10)
        yield env.timeout(1)

def run_simulation(scenario):
    env = simpy.Environment()
    disaster_scenario = {'resources': [{'name': 'Water', 'available': 100}, {'name': 'Food', 'available': 200}]}
    
    env.process(simulate_disaster(env, disaster_scenario))
    env.run(until=10)
    return np.random.uniform(1, 10)  # Simulated response time
