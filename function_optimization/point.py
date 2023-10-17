import matplotlib


class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def plot(self, ax: matplotlib.axes.Axes, highlight: bool = False) -> None:
        color = 'red' if highlight else 'black'
        ax.scatter(self.x, self.y, self.z, color=color, zorder=1)
