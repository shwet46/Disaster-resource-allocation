from deap import base, creator, tools, algorithms
import numpy as np

# Define the genetic algorithm for resource allocation
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def evaluate(individual):
    return sum(individual),  # Objective function: minimize total resources

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, 0, 100)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def run_ga(scenario):
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, halloffame=hof, verbose=False)
    
    best_individual = hof[0]
    return {f"resource_{i}": int(v) for i, v in enumerate(best_individual)}
