import click

from cities import cities as all_cities
from algorithm.genetic import genetic_travelling_salesman
from algorithm.ant_colony import ant_colony


@click.command()
@click.option('--number_of_cities', default=10, type=click.IntRange(2, len(all_cities)),
              help='Number of cities to visit.')
@click.option('--number_of_generations', default=200, help='Number of generations.')
@click.option('--number_of_individuals', default=20, help='Number of individuals in population.')
@click.option('--plot', default=True, help='Plot the algorithm progress.')
def main(**kwargs) -> None:
    best_route = ant_colony(**kwargs)
    print(f'Best route: {best_route.route}')
    print(f'Distance: {best_route.distance}')


if __name__ == "__main__":
    main()
