from functions.function import Function
from algorithm.algorithm import Algorithm
from point import Point
import numpy as np


class Particle:
    def __init__(self, position: Point, velocity: np.ndarray):
        self.position = position
        self.best_position = position
        self.velocity = velocity

    def move(self, function: Function) -> None:
        new_coords = [self.position[i] + self.velocity[i] for i in range(self.position.dimension - 1)]
        new_coords.append(function.get_value(*new_coords))
        new_point = Point(*new_coords)
        self.position = function.move_to_function_range(new_point)

    def check_and_set_new_best_position(self) -> bool:
        is_better = self.position.value < self.best_position.value
        if is_better:
            self.best_position = self.position
        return is_better


class ParticleSwarm(Algorithm):
    def __init__(self,
                 function: Function,
                 number_of_individuals: int = 10,
                 number_of_migration_cycles: int = 100,
                 min_velocity: float = -1,
                 max_velocity: float = 1):
        self.number_of_individuals = number_of_individuals
        self.number_of_migration_cycles = number_of_migration_cycles
        self.generation_number = 0
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.c1 = self.c2 = 2
        super().__init__(function)
        self.init_algorithm()

    def init_algorithm(self) -> list:
        population = [Particle(self.best_point, self.generate_random_velocity(self.best_point.dimension))]
        for _ in range(self.number_of_individuals - 1):
            point = self.function.get_random_point()
            if point.value < self.best_point.value:
                self.best_point = point
            population.append(Particle(point, self.generate_random_velocity(point.dimension)))
        self.found_points.append(self.best_point)
        self.population = population

    def generate_random_velocity(self, dimension: int) -> np.ndarray:
        return np.random.uniform(self.min_velocity, self.max_velocity, dimension)

    def get_new_velocity(self, particle: Particle):
        w = 0.9 - 0.5 * (self.generation_number / self.number_of_migration_cycles)
        r1 = np.random.uniform()
        a = particle.velocity * w
        b = (particle.best_position - particle.position) * self.c1 * r1
        c = (self.best_point - particle.position) * r1 * self.c2
        v = b + c + a
        v.min(self.min_velocity)
        v.max(self.max_velocity)
        return v

    def generate_next_solutions(self) -> None:
        if self.generation_number >= self.number_of_migration_cycles:
            return
        self.found_points = []
        for i, x in enumerate(self.population):
            x.move(self.function)
            if x.check_and_set_new_best_position():
                if x.position.value < self.best_point.value:
                    self.best_point = x.position
            x.velocity = self.get_new_velocity(x)
            self.found_points.append(x.position)
        self.generation_number += 1
