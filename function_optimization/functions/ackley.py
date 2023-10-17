from functions.function import Function
import numpy as np
from typing import Tuple


class Ackley(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -32.768, 32.768

    @property
    def y_range(self) -> Tuple[float, float]:
        return -32.768, 32.768

    def get_value(self, x: float, y: float) -> float:
        a = 20
        b = 0.2
        c = 2 * np.pi
        sum1 = x ** 2 + y ** 2
        sum2 = np.cos(c * x) + np.cos(c * y)
        return -a * np.exp(-b * np.sqrt(sum1 / 2)) - np.exp(sum2 / 2) + a + np.exp(1)

    def title(self) -> str:
        return 'Ackley Function'
