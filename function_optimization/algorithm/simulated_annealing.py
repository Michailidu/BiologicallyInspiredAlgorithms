from functions.function import Function
from algorithm.algorithm import Algorithm
import numpy as np


class SimulatedAnnealing(Algorithm):
    def __init__(self, function: Function,
                 temperature: float = 100,
                 cooling_rate: float = 0.05,
                 min_temperature: float = 0.5):
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        super().__init__(function)

    def generate_next_solutions(self) -> None:
        if self.temperature < self.min_temperature:
            return
        neighbour = self.function.get_neighbour(self.best_point)
        self.found_points.append(neighbour)
        if neighbour.value < self.best_point.value:
            self.best_point = neighbour
        else:
            probability = np.exp(-(neighbour.value - self.best_point.value) / self.temperature)
            if np.random.rand() < probability:
                self.best_point = neighbour
        self.temperature *= 1 - self.cooling_rate
        self.text = f'Temperature: {self.temperature:.2f}'
