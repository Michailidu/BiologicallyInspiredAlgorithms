from functions.function import Function
from algorithm.algorithm import Algorithm
from point import Point
import numpy as np


class DifferentialEvolution(Algorithm):
    def __init__(self,
                 function: Function,
                 number_of_individuals: int = 4,        # NP
                 number_of_generations: int = 100,      # G_maxim
                 mutation_constant: float = 0.5,        # F
                 crossover_range: float = 0.5):         # CR
        self.generation_number = None
        self.population = None
        self.number_of_individuals = number_of_individuals
        self.number_of_generations = number_of_generations
        self.mutation_constant = mutation_constant
        self.crossover_range = crossover_range
        super().__init__(function)
        self.init_algorithm()

    def initialize_population(self, number_of_individuals: int) -> list:
        population = [self.best_point]
        for _ in range(number_of_individuals - 1):
            point = self.function.get_random_point()
            if point.value < self.best_point.value:
                self.best_point = point
            population.append(self.function.get_random_point())
        self.found_points.append(self.best_point)
        return population

    def init_algorithm(self) -> None:
        self.population = self.initialize_population(self.number_of_individuals)
        self.generation_number = 0

    def get_new_population_individual(self, individual: Point) -> Point:
        r1, r2, r3 = np.random.choice(self.number_of_individuals, 3, replace=False)
        x_r1, x_r2, x_r3 = self.population[r1], self.population[r2], self.population[r3]
        v = (x_r1 - x_r2) * self.mutation_constant + x_r3
        u = [0, 0]
        random_index = np.random.randint(individual.dimension)
        for j in range(individual.dimension - 1):
            if np.random.uniform() < self.crossover_range or j == random_index:
                u[j] = v[j]
            else:
                u[j] = individual[j]
        u = Point(*u, self.function.get_value(*u))
        if u.value < individual.value:
            return u
        return individual

    def note_current_best_point(self):
        for individual in self.population:
            if individual.value < self.best_point.value:
                self.best_point = individual
        self.found_points.append(self.best_point)

    def generate_next_solutions(self) -> None:
        if self.generation_number >= self.number_of_generations:
            return
        new_population = self.population.copy()
        for i, individual in enumerate(self.population):
            new_population[i] = self.get_new_population_individual(individual)
        self.population = new_population

        self.note_current_best_point()

        self.text = f'Generation: {self.generation_number}'
        self.generation_number += 1
