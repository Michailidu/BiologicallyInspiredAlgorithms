from random import random, choice
from matplotlib import pyplot as plt, animation
from cities import cities as all_cities
from plot import plot_best_individual, prepare_figure
from initialize import initialize_population, initialize_distance_matrix, initialize_cities_with_coordinates
from evaluate import EvaluatedIndividual, evaluate_population, evaluate_individual, get_best_individual


def initialize_pheromone_matrix(cities: list) -> dict:
    """Initialize pheromone matrix between cities."""
    pheromone_matrix = {}
    for city in cities:
        pheromone_matrix[city] = {}
        for other_city in cities:
            if city != other_city:
                pheromone_matrix[city][other_city] = 1
    return pheromone_matrix


def initialize_visibility_matrix(distance_matrix: dict, initial_city: str) -> dict:
    """Initialize visibility matrix between cities."""
    visibility_matrix = {}
    for city, distances in distance_matrix.items():
        visibility_matrix[city] = {}
        for other_city, distance in distances.items():
            if other_city == initial_city:
                visibility_matrix[city][other_city] = 0
            else:
                visibility_matrix[city][other_city] = 1 / distance
    return visibility_matrix


def cumulative_probabilities(probabilities: dict) -> dict:
    """Calculate cumulative probabilities."""
    cumulative = {}
    total = sum(probabilities.values())
    probabilities_sum = 0
    for city, probability in probabilities.items():
        cumulative_probability = probabilities_sum + probability / total
        probabilities_sum += probability / total
        cumulative[city] = cumulative_probability
    return cumulative


def get_next_city(visited_cities: list, pheromone_matrix: dict, visibility_matrix: dict) -> str:
    """Get next city based on pheromone and visibility matrices."""
    current_city = visited_cities[-1]

    probabilities = {}
    for city, pheromone in pheromone_matrix[current_city].items():
        if city not in visited_cities:
            ni = visibility_matrix[current_city][city]
            probabilities[city] = (pheromone * ni * ni)

    cumulative = cumulative_probabilities(probabilities)
    random_number = random()
    for city, probability in cumulative.items():
        if random_number <= probability:
            return city

    return None


def make_invisible(city: str, visibility_matrix: dict) -> dict:
    """Make city invisible in visibility matrix."""
    for other_city in visibility_matrix:
        visibility_matrix[other_city][city] = 0
    return visibility_matrix


def vaporize_pheromone(pheromone_matrix: dict) -> dict:
    """Vaporize pheromone by half."""
    for city, pheromones in pheromone_matrix.items():
        for other_city, pheromone in pheromones.items():
            pheromone_matrix[city][other_city] = pheromone / 2
    return pheromone_matrix


def update_pheromone_matrix(evaluated_ants: list, pheromone_matrix: dict) -> dict:
    """Update pheromone matrix based on ants paths."""
    for ant in evaluated_ants:
        for i in range(len(ant.route) - 1):
            current_city = ant.route[i]
            next_city = ant.route[i + 1]
            current_pheromone = pheromone_matrix[current_city][next_city]
            pheromone_matrix[current_city][next_city] = current_pheromone + 1 / ant.distance
    return pheromone_matrix


def ant_colony(number_of_cities: int,
               number_of_generations: int,
               number_of_individuals: int,
               plot: bool = True) -> EvaluatedIndividual:
    """Ant Colony Optimization algorithm for solving travelling salesman problem."""
    cities = all_cities[:number_of_cities]
    cities_with_coordinates = initialize_cities_with_coordinates(cities)
    distance_matrix = initialize_distance_matrix(cities_with_coordinates)

    pheromone_matrix = initialize_pheromone_matrix(cities)

    def update(i):
        nonlocal distance_matrix, cities_with_coordinates, number_of_individuals, \
            number_of_generations, pheromone_matrix, ax
        ants = []
        for j in range(number_of_individuals):
            initial_city = choice(cities)
            visibility_matrix = initialize_visibility_matrix(distance_matrix, initial_city)
            offspring = [initial_city]
            for k in range(len(cities) - 2):
                next_city = get_next_city(offspring, pheromone_matrix, visibility_matrix)
                offspring.append(next_city)
                visibility_matrix = make_invisible(next_city, visibility_matrix)
            offspring.append([city for city in cities if city not in offspring][0])
            ants.append(offspring)
        evaluated_ants = evaluate_population(ants, distance_matrix)
        pheromone_matrix = vaporize_pheromone(pheromone_matrix)
        pheromone_matrix = update_pheromone_matrix(evaluated_ants, pheromone_matrix)

        best_individual = get_best_individual(evaluated_ants)
        plot_best_individual(best_individual.route, best_individual.distance, cities_with_coordinates, i, ax)

    if plot:
        fig, ax = prepare_figure()
        anim = animation.FuncAnimation(fig, update, frames=number_of_generations, interval=10, repeat=False)
        plt.show()
    else:
        for i in range(number_of_generations):
            update(i)
    return get_best_individual(evaluated_population)
