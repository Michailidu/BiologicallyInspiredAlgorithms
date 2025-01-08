import matplotlib
from matplotlib import pyplot as plt


def prepare_figure() -> tuple:
    """Prepare figure and axes for plotting."""
    matplotlib.use('TkAgg')
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return fig, ax


def plot_best_individual(best_route: list,
                         best_distance: float,
                         cities_with_coordinates: dict,
                         i: int,
                         ax: plt.Axes) -> None:
    """Plot the best individual in current generation."""

    x, y = zip(*[cities_with_coordinates[city] for city in best_route])

    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    ax.clear()
    ax.plot(x, y, 'o-')
    for city, x_coord, y_coord in zip(best_route, x, y):
        ax.text(x_coord + 0.01, y_coord, city)
    ax.set_title(f'Best route (distance: {best_distance:.2f})')
    ax.set_xlabel(f'Generation: {i + 1}')