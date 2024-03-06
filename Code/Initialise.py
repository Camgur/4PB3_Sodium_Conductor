from ase import units
from ase import atoms
from ase.io import read, write
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np
import torch

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
init_conf = read('/home/camgur/Documents/Coding/Chem_4PB3/Na4Sn2Ge5O16_filthy.xyz', '0')
init_conf.cell = [6.50630, 11.91200, 18.99500]
init_conf.set_pbc(True) # Set as repeating boundary periodic
init_conf.set_calculator(calculator)
print(init_conf)

e = init_conf.get_potential_energy()
# print(e)

forces = init_conf.get_forces()
# print(forces)

positions = init_conf.get_positions()
# print(positions)

formula = init_conf.get_chemical_formula()
# print(formula)



# Run geometry optimisation from MACE forces
dyn = BFGS(init_conf, trajectory='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Un_Filthify.traj')
def write():
        dyn.atoms.write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Un_Filthied.xyz')
dyn.attach(write)
dyn.run(fmax=0.05)