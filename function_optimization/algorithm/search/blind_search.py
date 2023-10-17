from algorithm.search.search import Search
from point import Point


class BlindSearch(Search):
    def get_new_solution(self) -> Point:
        return self.function.get_random_point()
