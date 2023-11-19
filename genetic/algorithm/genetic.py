from random import randint
import numpy as np
from matplotlib import pyplot as plt, animation
from cities import cities as all_cities
from plot import plot_best_individual, prepare_figure
from initialize import initialize_population, initialize_distance_matrix, initialize_cities_with_coordinates
from evaluate import EvaluatedIndividual, evaluate_population, evaluate_individual, get_best_individual


def crossover(parent_a: EvaluatedIndividual, parent_b: EvaluatedIndividual) -> list:
    """Crossover two individuals to get offspring. Get first half of the first parent's route and fill the rest with
    the cities from the second parent's route. """
    offspring = parent_a.route[:len(parent_a.route) // 2]
    for city in parent_b.route:
        if city not in offspring and len(offspring) < len(parent_a.route):
            offspring.append(city)

    return offspring


def mutate(offspring: list) -> list:
    """Swap two random cities in the route."""
    random_id_1 = randint(0, len(offspring) - 1)
    random_id_2 = randint(0, len(offspring) - 2)
    random_id_2 = random_id_2 + 1 if random_id_2 >= random_id_1 else random_id_2
    offspring[random_id_1], offspring[random_id_2] = offspring[random_id_2], offspring[random_id_1]
    return offspring


def genetic_travelling_salesman(number_of_cities: int,
                                number_of_generations: int,
                                number_of_individuals: int,
                                plot: bool = True) -> EvaluatedIndividual:
    """Genetic algorithm for solving travelling salesman problem."""
    cities = all_cities[:number_of_cities]
    cities_with_coordinates = initialize_cities_with_coordinates(cities)
    distance_matrix = initialize_distance_matrix(cities_with_coordinates)

    population = initialize_population(cities, number_of_individuals)
    evaluated_population = evaluate_population(population, distance_matrix)

    def update(i):
        nonlocal evaluated_population, distance_matrix, cities_with_coordinates, number_of_individuals, \
            number_of_generations, ax
        new_population = evaluated_population.copy()
        for j in range(number_of_individuals):
            parent_a = new_population[j]
            random_id = randint(0, number_of_individuals - 2)
            parent_b = new_population[random_id + 1] if random_id >= j else new_population[random_id]
            offspring = crossover(parent_a, parent_b)
            if np.random.uniform() < 0.5:
                offspring = mutate(offspring)
            evaluated_offspring = evaluate_individual(offspring, distance_matrix)

            if evaluated_offspring.distance < parent_a.distance:
                new_population[j] = evaluated_offspring
        evaluated_population = new_population

        best_individual = get_best_individual(evaluated_population)
        plot_best_individual(best_individual.route, best_individual.distance, cities_with_coordinates, i, ax)

    if plot:
        fig, ax = prepare_figure()
        anim = animation.FuncAnimation(fig, update, frames=number_of_generations, interval=10, repeat=False)
        plt.show()
    else:
        for j in range(number_of_generations):
            update(j)
    return get_best_individual(evaluated_population)
