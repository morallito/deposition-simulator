from plotter.plotter import Plotter
from random_deposition.random_deposition_simulator import RandomDeposition



my_plotter = Plotter(500, 100)
simulator = RandomDeposition(500,100)

simulator.simulate()
A = simulator.get_output_matrix()
my_plotter.set_matrix(A)
my_plotter.plot('sim_test')


