import click
from algorithm.algorithm import Algorithm
from algorithm.search.blind_search import BlindSearch
from algorithm.search.hill_climbing import HillClimbing
from algorithm.simulated_annealing import SimulatedAnnealing
from algorithm.differential_evolution import DifferentialEvolution
from algorithm.particle_swarm import ParticleSwarm
from algorithm.SOMA import SOMA
from algorithm.firefly import FireflyAlgorithm

from functions.function import Function
from functions.ackley import Ackley
from functions.sphere import Sphere
from functions.schwefel import Schwefel
from functions.rosenbrock import Rosenbrock
from functions.rastrigin import Rastrigin
from functions.griewank import Griewank
from functions.levy import Levy
from functions.michalewicz import Michalewicz
from functions.zakharov import Zakharov
from animation import Animation
import matplotlib as matplotlib


def update_function(algorithm: Algorithm):
    def update(i: int) -> matplotlib.axes.Axes:
        ax = algorithm.animate()
        return ax
    return update


function_map = {
    'Ackley': Ackley,
    'Sphere': Sphere,
    'Schwefel': Schwefel,
    'Rosenbrock': Rosenbrock,
    'Rastrigin': Rastrigin,
    'Griewank': Griewank,
    'Levy': Levy,
    'Michalewicz': Michalewicz,
    'Zakharov': Zakharov
}


algorithm_map = {
    'BlindSearch': BlindSearch,
    'HillClimbing': HillClimbing,
    'SimulatedAnnealing': SimulatedAnnealing,
    'DifferentialEvolution': DifferentialEvolution,
    'ParticleSwarm': ParticleSwarm,
    'SOMA': SOMA,
    'Firefly': FireflyAlgorithm
}


def map_string_to_class(name, class_map) -> callable:
    return class_map.get(name)


@click.command()
@click.option('--algorithm',
              type=click.Choice(['BlindSearch',
                                 'HillClimbing',
                                 'SimulatedAnnealing',
                                 'DifferentialEvolution',
                                 'ParticleSwarm',
                                 'SOMA',
                                 'Firefly']),
              default='Firefly',
              help='Algorithm to use.')
@click.option('--function',
              type=click.Choice(['Ackley', 'Sphere', 'Schwefel', 'Rosenbrock', 'Rastrigin', 'Griewank', 'Levy',
                                 'Michalewicz', 'Zakharov']),
              default='Ackley',
              help='Function to run the algorithm on.')
def main(algorithm, function):
    matplotlib.use('TkAgg')

    function = map_string_to_class(function, function_map)()
    algorithm = map_string_to_class(algorithm, algorithm_map)(function)

    animation = Animation(100, update_function(algorithm))
    animation.animate()


if __name__ == '__main__':
    main()
