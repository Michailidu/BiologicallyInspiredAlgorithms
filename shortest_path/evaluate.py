from collections import namedtuple

EvaluatedIndividual = namedtuple('EvaluatedIndividual', ['route', 'distance'])


def evaluate_individual(individual: list, distance_matrix: dict) -> EvaluatedIndividual:
    """Get distance of the route of the individual."""
    distance = 0
    for i in range(len(individual) - 1):
        distance += distance_matrix[individual[i]][individual[i + 1]]
    distance += distance_matrix[individual[-1]][individual[0]]
    return EvaluatedIndividual(individual, distance)


def evaluate_population(population: list, distance_matrix: dict) -> list:
    """Get distances of the routes of the individuals in the population."""
    evaluated_population = []
    for individual in population:
        evaluated_population.append(evaluate_individual(individual, distance_matrix))
    return evaluated_population


def get_best_individual(evaluated_population: list) -> EvaluatedIndividual:
    """Get the individual with the shortest route."""
    return min(evaluated_population, key=lambda x: x.distance)
