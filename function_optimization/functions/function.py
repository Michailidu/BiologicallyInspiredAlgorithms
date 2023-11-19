from abc import ABC, abstractmethod
import numpy as np
from point import Point
from typing import Tuple


class Function(ABC):
    @abstractmethod
    def get_value(self, x: float, y: float) -> float:
        pass

    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @property
    @abstractmethod
    def x_range(self) -> Tuple[float, float]:
        pass

    @property
    @abstractmethod
    def y_range(self) -> Tuple[float, float]:
        pass

    @property
    def scale_x(self) -> float:
        return (self.x_range[1] - self.x_range[0]) / 20

    @property
    def scale_y(self) -> float:
        return (self.y_range[1] - self.y_range[0]) / 20

    def move_to_function_range(self, point: Point) -> Point:
        x = self.x_range[1] if point[0] < self.x_range[0] else point[0]
        x = self.x_range[0] if x > self.x_range[1] else x
        y = self.y_range[1] if point[1] < self.y_range[0] else point[1]
        y = self.y_range[0] if y > self.y_range[1] else y
        return Point(x, y, self.get_value(x, y))

    def plot(self, ax) -> None:
        x_vals = np.linspace(*self.x_range, 100)
        y_vals = np.linspace(*self.y_range, 100)
        x, y = np.meshgrid(x_vals, y_vals)
        z = self.get_value(x, y)
        ax.plot_surface(x, y, z, cmap='viridis', alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('f(x, y)')
        ax.set_title(self.title())

    def get_random_point(self) -> Point:
        x = np.random.uniform(*self.x_range)
        y = np.random.uniform(*self.y_range)
        z = self.get_value(x, y)
        return Point(x, y, z)

    def get_neighbour(self, point: Point) -> Point:
        x = None
        while x is None or x < self.x_range[0] or x > self.x_range[1]:
            x = np.random.normal(loc=point.x, scale=self.scale_x)
        y = None
        while y is None or y < self.y_range[0] or y > self.y_range[1]:
            y = np.random.normal(loc=point.y, scale=self.scale_y)
        return Point(x, y, self.get_value(x, y))

    def get_evaluated(self, point: Point) -> Point:
        return Point(*point.coordinates, self.get_value(*point.coordinates))