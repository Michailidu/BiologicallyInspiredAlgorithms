import matplotlib
import numpy as np


class Point:
    def __init__(self, *args):
        self.coordinates = list(args)

    def plot(self, ax: matplotlib.axes.Axes, highlight: bool = False) -> None:
        color = 'red' if highlight else 'black'
        ax.scatter(*self.coordinates, color=color)

    @property
    def value(self) -> float:
        return self.coordinates[-1]

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    def min(self, min_value: float) -> None:
        for i in range(self.dimension):
            if self.coordinates[i] < min_value:
                self.coordinates[i] = min_value

    def max(self, max_value: float) -> None:
        for i in range(self.dimension):
            if self.coordinates[i] > max_value:
                self.coordinates[i] = max_value

    def __add__(self, other: any) -> 'Point':
        if isinstance(other, float) or isinstance(other, int):
            return self + Point(*[other for _ in range(self.dimension)])
        if isinstance(other, np.ndarray):
            return self + Point(*other)
        if isinstance(other, Point):
            if self.dimension != other.dimension:
                raise ValueError('Dimensions of points are not equal')
            new_coordinates = []
            for i in range(self.dimension):
                new_coordinates.append(self.coordinates[i] + other.coordinates[i])
            return Point(*new_coordinates)
        raise TypeError('Unsupported type for addition')

    def __sub__(self, other: 'Point') -> 'Point':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions of points are not equal')
        new_coordinates = []
        for i in range(self.dimension):
            new_coordinates.append(self.coordinates[i] - other.coordinates[i])
        return Point(*new_coordinates)

    def __mul__(self, other: any) -> 'Point':
        new_coordinates = []
        if isinstance(other, Point):
            if self.dimension != other.dimension:
                raise ValueError('Dimensions of points are not equal')
            for i in range(self.dimension):
                new_coordinates.append(self.coordinates[i] * other.coordinates[i])
            return Point(*new_coordinates)
        if isinstance(other, float) or isinstance(other, int):
            for i in range(self.dimension):
                new_coordinates.append(self.coordinates[i] * other)
            return Point(*new_coordinates)
        raise TypeError('Unsupported type for multiplication')

    def __getitem__(self, item):
        if item < 0 or item >= self.dimension:
            raise IndexError('Index out of range')
        return self.coordinates[item]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.dimension:
            raise IndexError('Index out of range')
        self.coordinates[key] = value
