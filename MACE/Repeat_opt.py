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


# Importing Intial Structure
atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_fixed.cif')
# Set calculator
calculator = MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda', default_dtype='float64')
atoms.calc = calculator
print(atoms.symbols, '\n')


# Set Savestate
trajsave = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Trajectories/Trajectory'
cifsave = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/TCIF/Crystal'


# Number of Interations
iter = 15


# Set Cell filter (preserve unit cell ratioe)
# atoms = ExpCellFilter(atoms, hydrostatic_strain=False)
atoms.set_constraint(FixSymmetry(atoms))

for i in range(iter):
    print('Iteration: ', i+1)
    # Set Savestate
    trajsave = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Trajectories/Trajectory_1_'
    trajsave += str(i)
    trajsave += '.traj'
    cifsave = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/TCIF/Crystal_1_'
    cifsave += str(i)
    cifsave += '.cif'

    # Rattle Positions
    atoms.rattle(1)

    # Optimise
    opt = BFGS(UnitCellFilter(atoms), trajectory=trajsave)
    opt.run(fmax=1e-4)
    atoms.write(cifsave)

    # Output Params
    print('\n\n')
    print("Cell size after : ", atoms.cell)
    print("Spacegroup: ", get_spacegroup((atoms.cell, atoms.get_scaled_positions(), atoms.numbers), symprec=1e-2))
    print('Iteration: ', i+1)



print('\n\nFinished!!!')