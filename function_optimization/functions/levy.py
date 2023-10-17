from functions.function import Function
import numpy as np
from typing import Tuple


class Levy(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -10, 10

    @property
    def y_range(self) -> Tuple[float, float]:
        return -10, 10

    def get_value(self, x: float, y: float) -> float:
        w = 1 + (x - 1) / 4
        h = 1 + (y - 1) / 4
        term1 = np.sin(np.pi * w) ** 2
        term2 = (w - 1) ** 2 * (1 + 10 * np.sin(np.pi * w + 1) ** 2)
        term3 = (h - 1) ** 2 * (1 + np.sin(2 * np.pi * h) ** 2)
        return term1 + term2 + term3

    def title(self) -> str:
        return 'Levy Function'
