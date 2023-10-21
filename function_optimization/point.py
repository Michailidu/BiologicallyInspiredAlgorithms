import matplotlib


class Point:
    def __init__(self, *args):
        self.coordinates = list(args)

    def plot(self, ax: matplotlib.axes.Axes, highlight: bool = False) -> None:
        color = 'red' if highlight else 'black'
        ax.scatter(*self.coordinates, color=color)
        # ax.scatter(self.x, self.y, self.z, color=color, zorder=1)


    @property
    def value(self) -> float:
        return self.coordinates[-1]

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    def __add__(self, other: 'Point') -> 'Point':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions of points are not equal')
        new_coordinates = []
        for i in range(self.dimension):
            new_coordinates.append(self.coordinates[i] + other.coordinates[i])
        return Point(*new_coordinates)

    def __sub__(self, other: 'Point') -> 'Point':
        if self.dimension != other.dimension:
            raise ValueError('Dimensions of points are not equal')
        new_coordinates = []
        for i in range(self.dimension):
            new_coordinates.append(self.coordinates[i] - other.coordinates[i])
        return Point(*new_coordinates)

    def __mul__(self, other: float) -> 'Point':
        new_coordinates = []
        for i in range(self.dimension):
            new_coordinates.append(self.coordinates[i] * other)
        return Point(*new_coordinates)

    def __getitem__(self, item):
        if item < 0 or item >= self.dimension:
            raise IndexError('Index out of range')
        return self.coordinates[item]

    def __setitem__(self, key, value):
        if key < 0 or key >= self.dimension:
            raise IndexError('Index out of range')
        self.coordinates[key] = value
