from functions.function import Function
from algorithm.algorithm import Algorithm
from point import Point
import numpy as np


class SOMA(Algorithm):
    def __init__(self,
                 function: Function,
                 population_size: int = 5,
                 prt: float = 0.4,
                 path_length: float = 3.0,
                 step_size: float = 0.11,
                 max_iterations: int = 100):
        self.population_size = population_size
        self.prt = prt
        self.path_length = path_length
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.population = None
        self.generation_number = 0
        super().__init__(function)
        self.initialize_population()

    def initialize_population(self) -> None:
        self.population = [self.function.get_random_point() for _ in range(self.population_size)]
        self.best_point = self.population[0]
        for point in self.population:
            if point.value < self.best_point.value:
                self.best_point = point
        self.found_points.append(self.best_point)

    def get_prt_vector(self, dimension: int) -> Point:
        prt_vector = Point(0, 0)
        while prt_vector[0] == 0 and prt_vector[1] == 0:
            for i in range(dimension):
                if np.random.uniform() < self.prt:
                    prt_vector[i] = 1
        return prt_vector

    def check_leader(self, individual: Point) -> Point:
        best_point = individual
        individual_coords = Point(individual[0], individual[1])
        leader_coords = Point(self.best_point[0], self.best_point[1])
        t = 0
        while t < self.path_length:
            prt_vector = self.get_prt_vector(individual_coords.dimension)
            new_point = individual_coords + prt_vector * (leader_coords - individual_coords) * t
            new_point = Point(*new_point, self.function.get_value(*new_point))
            new_point = self.function.move_to_function_range(new_point)
            if new_point.value < best_point.value:
                best_point = new_point
            t += self.step_size
        return best_point

    def set_new_leader(self, new_population: list) -> None:
        self.best_point = new_population[0]
        for individual in new_population:
            if individual.value < self.best_point.value:
                self.best_point = individual

    def generate_next_solutions(self) -> None:
        if self.generation_number >= self.max_iterations:
            return
        new_population = []
        self.found_points = []
        for individual in self.population:
            best_point = self.check_leader(individual)
            new_population.append(best_point)
            self.found_points.append(best_point)
        self.set_new_leader(new_population)
        self.population = new_population
        self.generation_number += 1



