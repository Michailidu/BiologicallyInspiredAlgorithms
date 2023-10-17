from functions.function import Function
import numpy as np
from typing import Tuple


class Griewank(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -600, 600

    @property
    def y_range(self) -> Tuple[float, float]:
        return -600, 600

    def get_value(self, x: float, y: float) -> float:
        return (x ** 2) / 4000 + (y ** 2) / 4000 - np.cos(x) * np.cos(y / np.sqrt(2)) + 1

    def title(self) -> str:
        return 'Griewank Function'
