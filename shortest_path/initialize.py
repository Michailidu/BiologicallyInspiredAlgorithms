from random import random, shuffle


def initialize_distance_matrix(cities_with_coordinates: dict) -> dict:
    """Initialize distance matrix between cities."""
    matrix = {}
    for city, (x, y) in cities_with_coordinates.items():
        distances = {}
        for other_city, (other_x, other_y) in cities_with_coordinates.items():
            if city != other_city:
                distance = ((x - other_x) ** 2 + (y - other_y) ** 2) ** 0.5
                distances[other_city] = distance
        matrix[city] = distances
    return matrix


def initialize_population(cities: list, number_of_individuals: int) -> list:
    """Initialize population of individuals with random order of cities."""
    population = []
    for i in range(number_of_individuals):
        population.append(cities.copy())
        shuffle(population[i])
    return population


def initialize_cities_with_coordinates(cities: list) -> dict:
    """Assign random coordinates to cities."""
    cities_with_coordinates = {}
    for city in cities:
        cities_with_coordinates[city] = (random(), random())
    return cities_with_coordinates
