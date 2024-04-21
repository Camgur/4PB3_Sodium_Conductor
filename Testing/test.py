from ase import units
from ase import atoms
from ase.io import read, write
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.optimize.precon import Exp, PreconLBFGS
import numpy as np
import torch

from ase.calculators.loggingcalc import LoggingCalculator
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from mace.calculators import MACECalculator

# PyTorch Memory Issue -- Change to disable caching (set PYTORCH_NO_CUDA_MEMORY_CACHING=1)
# https://pytorch.org/docs/2.0/notes/hip.html

# SchNetPack
# https://schnetpack.readthedocs.io/en/latest/getstarted.html

# ASE Calculator
# https://wiki.fysik.dtu.dk/ase/ase/

# MACE Initialisation
# https://mace-docs.readthedocs.io/en/latest/guide/

# Set the calulation parameters
calculator = MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda', default_dtype='float64')
atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_Fixed.xyz', '0')

# Set unit cell
atoms.cell = [6.50630, 11.91200, 18.99500]
# init_conf.set_pbc(True) # Set as repeating boundary periodic
atoms.set_calculator(calculator)
print(atoms)

nsteps = []
energies = []
log_calc = LoggingCalculator(calculator)


   
atoms.calc = log_calc
opt = BFGS(atoms, trajectory='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Test.traj')
def write():
    opt.atoms.write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Test.xyz')
opt.attach(write)
opt.run(fmax=1e-3, steps=200)

log_calc.plot(markers=['r-', 'b-'], energy=False, lw=2)

plt.show()