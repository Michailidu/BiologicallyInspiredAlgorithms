from algorithm.search.search import Search
from point import Point


class HillClimbing(Search):
    def get_new_solution(self) -> Point:
        return self.function.get_neighbour(self.best_point)
