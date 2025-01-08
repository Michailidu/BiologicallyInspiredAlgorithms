from abc import abstractmethod

from algorithm.algorithm import Algorithm
from functions.function import Function
from point import Point


class Search(Algorithm):
    def __init__(self, function: Function, step_size: int = 1):
        self.step_size = step_size
        super().__init__(function)

    def generate_next_solutions(self) -> None:
        # generate random solutions
        solutions = []
        for _ in range(self.step_size):
            solutions.append(self.get_new_solution())

        self.found_points.extend(solutions)

        # evaluate solutions and select the best one
        best_point_from_solutions = None
        for point in solutions:
            if best_point_from_solutions is None or point.z <= best_point_from_solutions.z:
                best_point_from_solutions = point

        # compare the previously found best solution with the current best solution and update if necessary
        if best_point_from_solutions.value < self.best_point.value:
            self.best_point = best_point_from_solutions

    @abstractmethod
    def get_new_solution(self) -> Point:
        pass
