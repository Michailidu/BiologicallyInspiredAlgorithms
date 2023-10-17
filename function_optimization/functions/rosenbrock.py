from functions.function import Function
from typing import Tuple


class Rosenbrock(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -5, 10

    @property
    def y_range(self) -> Tuple[float, float]:
        return -5, 10

    def get_value(self, x: float, y: float) -> float:
        return 100 * (y - x ** 2) ** 2 + (x - 1) ** 2

    def title(self) -> str:
        return 'Rosenbrock Function'
