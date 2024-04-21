from ase.io import read, write
from ase.visualize import view
from ase.io.trajectory import Trajectory

from mace.calculators import MACECalculator

traj = Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation.traj')

write(images=traj[-1], filename='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimised.cif')