from functions.function import Function
from algorithm.algorithm import Algorithm
from point import Point
import numpy as np


class Firefly:
    def __init__(self, point: Point):
        if point.dimension == 2:
            self.point = point
        else:
            self.point = Point(point[0], point[1])
        self.attractiveness = 1

    def light_intensity(self, other_firefly: 'Firefly', function: Function) -> float:
        gamma = 3
        distance = self.point.distance(other_firefly.point)
        light_intensity_0 = function.get_value(*self.point.coordinates)
        if distance == 0:
            return light_intensity_0
        return light_intensity_0 * np.exp(-gamma * distance)

    def value(self, function: Function) -> float:
        return function.get_value(*self.point.coordinates)


class FireflyAlgorithm(Algorithm):
    def __init__(self,
                 function: Function,
                 population_size: int = 5,
                 max_iterations: int = 100):
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.generation_number = 0
        self.population = []
        super().__init__(function)
        self.initialize_population()

    def set_best_point(self) -> None:
        self.best_point = min(self.found_points, key=lambda x: x.value)

    def set_found_points(self) -> None:
        self.found_points = [self.function.get_evaluated(firefly.point) for firefly in self.population]

    def initialize_population(self) -> None:
        self.population = [Firefly(self.function.get_random_point()) for _ in range(self.population_size)]
        self.set_found_points()
        self.set_best_point()

    def move_firefly(self, firefly: Firefly, other_firefly: Firefly) -> Firefly:
        alpha = 0.3
        attractiveness = other_firefly.attractiveness / (1 + firefly.point.distance(other_firefly.point))
        direction = other_firefly.point - firefly.point
        random_vector = Point(np.random.uniform(0, 1), np.random.uniform(0, 1))
        movement = direction * attractiveness + random_vector * alpha
        new_position = firefly.point + movement
        new_position = self.function.move_to_function_range(new_position)
        new_firefly = Firefly(new_position)
        return new_firefly

    def move_firefly_randomly(self, firefly: Firefly) -> Firefly:
        direction = Point(np.random.uniform(-1, 1), np.random.uniform(-1, 1))
        new_position = firefly.point + direction
        new_position = self.function.move_to_function_range(new_position)
        if self.function.get_value(new_position.coordinates[0], new_position.coordinates[1]) < \
                firefly.value(self.function):
            return Firefly(new_position)
        else:
            return firefly

    def generate_next_solutions(self) -> None:
        if self.generation_number == 0:
            self.generation_number += 1
            return
        if self.generation_number >= self.max_iterations:
            return
        new_population = []
        for firefly in self.population:
            for other_firefly in self.population:
                if firefly == other_firefly:
                    continue
                if firefly.value(self.function) == self.best_point.value:
                    firefly = self.move_firefly_randomly(firefly)
                elif firefly.value(self.function) > other_firefly.value(self.function):
                    firefly = self.move_firefly(firefly, other_firefly)
            new_population.append(firefly)

        self.population = new_population
        self.set_found_points()
        self.set_best_point()
        self.generation_number += 1
