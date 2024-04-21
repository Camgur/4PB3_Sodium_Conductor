from ase import units
from ase import atoms
from ase.io import read, write
from ase.optimize import BFGS
import numpy as np
import torch

from ase.visualize import view
from ase.io import Trajectory

from ase.constraints import ExpCellFilter, StrainFilter, UnitCellFilter
from ase.spacegroup.symmetrize import FixSymmetry, check_symmetry
from spglib import get_spacegroup
from ase.calculators.loggingcalc import LoggingCalculator
import matplotlib as mpl
import matplotlib.pyplot as plt

from mace.calculators import MACECalculator

'''

ASE Calculator
https://wiki.fysik.dtu.dk/ase/ase/

MACE Initialisation
https://mace-docs.readthedocs.io/en/latest/guide/


Optimisation Using ASE
https://docs.matlantis.com/atomistic-simulation-tutorial/en/2_1_opt.html

https://docs.matlantis.com/atomistic-simulation-tutorial/en/2_2_opt_symmetry.html


'''


# Importing Stuff
calculator = MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda', default_dtype='float64')
atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_fixed.cif')


# Set Calculator
atoms.calc = calculator
print(atoms.symbols, '\n')


# Track Data
nsteps = []
energies = []
log_calc = LoggingCalculator(calculator)


# Set Log
atoms.calc = log_calc


# Set Cell filter (preserve unit cell ratioe)
# atoms = ExpCellFilter(atoms, hydrostatic_strain=False)
atoms.set_constraint(FixSymmetry(atoms))

# Rattle Positions
atoms.rattle(3)
print(atoms.cell, '\n')
print("Cell size before: ", atoms.cell)
print("Spacegroup: ", get_spacegroup((atoms.cell, atoms.get_scaled_positions(), atoms.numbers), symprec=1e-2))
print('\n\n\n')
# print(check_symmetry(atoms))


# Optimise
opt = BFGS(UnitCellFilter(atoms), trajectory='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation_3.traj')


# Write Outputs
# def write():
#     opt.atoms.write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation_fixed.xyz')
# opt.attach(write)

# Run Optimise
opt.run(fmax=1e-4)
print('\n\n')
print("Cell size after : ", atoms.cell)
print("Spacegroup: ", get_spacegroup((atoms.cell, atoms.get_scaled_positions(), atoms.numbers), symprec=1e-2))
atoms.write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation_3.cif')


# Plot Out
log_calc.plot(markers=['r-', 'b-'], energy=True, lw=2)
plt.show()

print('Finished!!!')