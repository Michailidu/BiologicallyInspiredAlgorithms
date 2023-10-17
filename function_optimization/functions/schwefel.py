from functions.function import Function
import numpy as np
from typing import Tuple


class Schwefel(Function):
    @property
    def x_range(self) -> Tuple[float, float]:
        return -500, 500

    @property
    def y_range(self) -> Tuple[float, float]:
        return -500, 500

    def get_value(self, x: float, y: float) -> float:
        return 418.9829 * 2 - x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))

    def title(self) -> str:
        return 'Schwefel Function'
