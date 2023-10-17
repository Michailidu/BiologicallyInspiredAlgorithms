from functions.function import Function
import numpy as np
from typing import Tuple


class Rastrigin(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -5.12, 5.12

    @property
    def y_range(self) -> Tuple[float, float]:
        return -5.12, 5.12

    def get_value(self, x: float, y: float) -> float:
        return 20 + x ** 2 - 10 * np.cos(2 * np.pi * x) + y ** 2 - 10 * np.cos(2 * np.pi * y)

    def title(self) -> str:
        return 'Rastrigin Function'
