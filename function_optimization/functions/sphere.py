from functions.function import Function
from typing import Tuple


class Sphere(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -5.12, 5.12

    @property
    def y_range(self) -> Tuple[float, float]:
        return -5.12, 5.12

    def get_value(self, x: float, y: float) -> float:
        return x ** 2 + y ** 2

    def title(self) -> str:
        return 'Sphere Function'
