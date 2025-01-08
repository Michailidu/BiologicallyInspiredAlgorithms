import click

from cities import cities as all_cities
from algorithm.genetic import genetic_travelling_salesman
from algorithm.ant_colony import ant_colony


def map_algorithm_string_to_class(name) -> callable:
    algorithm_map = {
        'Genetic': genetic_travelling_salesman,
        'AntColony': ant_colony
    }
    return algorithm_map.get(name)


@click.command()
@click.option('--algorithm',
              type=click.Choice(['Genetic', 'AntColony']),
              default='Genetic',
              help='Algorithm to use.')
@click.option('--number_of_cities', default=15, type=click.IntRange(2, len(all_cities)),
              help='Number of cities to visit.')
@click.option('--number_of_generations', default=200, help='Number of generations.')
@click.option('--number_of_individuals', default=40, help='Number of individuals in population.')
@click.option('--plot', default=True, help='Plot the algorithm progress.')
def main(algorithm, **kwargs) -> None:
    best_route = map_algorithm_string_to_class(algorithm)(**kwargs)
    print(f'Best route: {best_route.route}')
    print(f'Distance: {best_route.distance}')


if __name__ == "__main__":
    main()
