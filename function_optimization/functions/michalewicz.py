from functions.function import Function
import numpy as np
from typing import Tuple


class Michalewicz(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return 0, np.pi

    @property
    def y_range(self) -> Tuple[float, float]:
        return 0, np.pi

    def get_value(self, x: float, y: float) -> float:
        m = 10
        term1 = -np.sin(x) * (np.sin(x ** 2 / np.pi)) ** (2 * m)
        term2 = -np.sin(y) * (np.sin(2 * y ** 2 / np.pi)) ** (2 * m)
        return term1 + term2

    def title(self) -> str:
        return 'Michalewicz Function'
