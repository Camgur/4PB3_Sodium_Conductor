import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase.visualize import view, ngl
from ase.io import Trajectory
import seaborn as sns
import numpy as np

# From: https://wiki.fysik.dtu.dk/ase/ase/visualize/visualize.html

# Set import and add atoms
sample_0 = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Sample_Crystals/Sample_0.cif')
sample_1 = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Sample_Crystals/Sample_1.cif')
sample_2 = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Sample_Crystals/Sample_2.cif')
sample_3 = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Sample_Crystals/Sample_3.cif')
sample_4 = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Sample_Crystals/Sample_4.cif')

# Set vectors
initialise = [sample_0, sample_1, sample_2, sample_3, sample_4]
initialised = ['Sample_0', 'Sample_1', 'Sample_2', 'Sample_3','Sample_4']

# Begin Plot
# fig, axarr = plt.subplots(len(initialise), 4, figsize=(12, 12))
# fig.suptitle('Comparison of Crystal Generation')

# for i in range(len(initialise)):
#     plot_atoms(initialise[i], axarr[i, 0], radii=0.3, rotation=('0x,0y,0z'))
#     plot_atoms(initialise[i], axarr[i, 1], scale=0.7, offset=(3, 4), radii=0.3, rotation=('0x,0y,0z'))
#     plot_atoms(initialise[i], axarr[i, 2], radii=0.3, rotation=('45x,45y,0z'))
#     plot_atoms(initialise[i], axarr[i, 3], radii=0.3, rotation=('0x,0y,0z'))
#     axarr[i, 0].set_title(initialised[i], fontsize=16, color='Red')
#     axarr[i, 1].set_xlabel("X-axis, [$\mathrm{\AA}$]")
#     axarr[i, 1].set_ylabel("Y-axis, [$\mathrm{\AA}$]")
#     axarr[i, 2].set_axis_off()
#     axarr[i, 3].set_xlim(0, 6)
#     axarr[i, 3].set_ylim(0, 6)

# plt.subplots_adjust(hspace=0.6)

# fig.savefig("/home/camgur/Documents/Coding/Chem_4PB3/Movies/Comparison_Crystals.png")
# plt.show()

for i in initialise:
    view(i)

# view(filth)

print('Finished!!!')