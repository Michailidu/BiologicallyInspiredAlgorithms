from typing import Tuple
from functions.function import Function


class Zakharov(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -5, 10

    @property
    def y_range(self) -> Tuple[float, float]:
        return -5, 10

    def get_value(self, x: float, y: float) -> float:
        term1 = x ** 2 + y ** 2
        term2 = 0.5 * x + y
        term3 = 0.5 * x + y
        return term1 + term2 ** 2 + term3 ** 4

    def title(self) -> str:
        return 'Zakharov Function'
