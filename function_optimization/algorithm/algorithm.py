from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
from functions.function import Function


class Algorithm(ABC):
    def __init__(self, function: Function):
        self.function = function
        # generate random initial solution
        initial_best_value = function.get_random_point()
        self.found_points = [initial_best_value]
        self.best_point = initial_best_value
        self.text = ""

    def plot(self, ax: plt.Axes) -> None:
        self.function.plot(ax)
        for point in self.found_points:
            point.plot(ax)
        if self.best_point is not None:
            self.best_point.plot(ax, highlight=True)
            plt.suptitle(f'Min: f({self.best_point.x:.2f}, {self.best_point.y:.2f}) = {self.best_point.z:.2f}'
                         f' {self.text}')

    def animate(self) -> plt.Axes:
        ax = plt.gca()
        ax.cla()
        self.generate_next_solutions()
        self.plot(ax)
        return ax

    @abstractmethod
    def generate_next_solutions(self) -> None:
        pass
