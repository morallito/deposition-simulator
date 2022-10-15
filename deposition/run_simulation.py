from plotter.plotter import Plotter
from random_deposition.random_deposition_simulator import RandomDeposition
from random_relaxed_deposition.relaxed_deposition import RelaxedDeposition
from balistic_deposition.balistic_deposition import BalisticDeposition


my_plotter = Plotter(500, 100)
simulator = RandomDeposition(500,100)

simulator.simulate()
A = simulator.get_output_matrix()
my_plotter.set_matrix(A)
my_plotter.plot('random_dep')




my_plotter = Plotter(200, 50)
simulator = RelaxedDeposition(200, 50)

simulator.simulate()
A = simulator.get_output_matrix()
my_plotter.set_matrix(A)
my_plotter.plot('relaxed_dep')


my_plotter = Plotter(500, 100)
simulator = BalisticDeposition(500,100)
simulator.simulate()
A = simulator.get_output_matrix()
my_plotter.set_matrix(A)
my_plotter.plot('balistic_dep')