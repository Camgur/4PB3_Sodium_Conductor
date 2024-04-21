import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase.visualize import view
import seaborn as sns
import numpy as np
from ase.io.trajectory import Trajectory

from mace.calculators import MACECalculator

atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimise.xyz')

# view(atoms, repeat=(3, 3, 2))

pristine = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Test.xyz')
pristine.set_calculator(MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda', default_dtype='float64'))

traj_2 = Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Test.traj')
traj = Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimise.traj')
atoms = traj[-1]
print('pristine potential:', pristine.get_potential_energy())
print('potential:', atoms.get_potential_energy())
print(len(traj))

# print(atoms.get_positions())
# print(atoms.get_potential_energy())

fig, ax = plt.subplots(figsize=(8,7), layout="tight")

for i in range(len(traj)):
    # print(i)
    # fit = np.poly1d(np.polyfit(i[:7, 5], i[:7, 6], deg=1))
    # ax.scatter(i[:, 5], i[:, 6], label=labels[n], marker=markers[n], color=colors[n], s=40)
    energy = traj[i]
    ax.scatter(i, energy.get_potential_energy(), color='teal', s=15)

for i in range(len(traj_2)):
    # print(i)
    # fit = np.poly1d(np.polyfit(i[:7, 5], i[:7, 6], deg=1))
    # ax.scatter(i[:, 5], i[:, 6], label=labels[n], marker=markers[n], color=colors[n], s=40)
    energy = traj_2[i]
    ax.scatter(i, energy.get_potential_energy(), color='orange', s=3)


ax.set_xlabel('Iterations (int)')
ax.set_ylabel(r'$E \; (eV)$')
ax.set_title('Potential Energy vs Iteration', pad=30)
# ax.legend()

# plt.show()

view(traj_2)