from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class Animation:
    def __init__(self, delay: int, update_function) -> None:
        self.delay = delay
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
        self.update_function = update_function

    def animate(self) -> None:
        anim = FuncAnimation(self.fig, self.update_function, interval=self.delay)
        plt.show()
