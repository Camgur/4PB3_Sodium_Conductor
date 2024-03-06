import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase.visualize import view
import seaborn as sns
import numpy as np

# From: https://wiki.fysik.dtu.dk/ase/ase/visualize/visualize.html

# Set atoms
de_filthied = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/De_Filthied.xyz', '0')
de_filthied.cell = [6.50630, 11.91200, 18.99500]
filth = read('/home/camgur/Documents/Coding/Chem_4PB3/Na4Sn2Ge5O16_filthy.xyz', '0')
filth.cell = [6.50630, 11.91200, 18.99500]
pristine = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16.xyz', '0')
pristine.cell = [6.50630, 11.91200, 18.99500]
de_pristined = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/De_Pristined.xyz', '0')
de_pristined.cell = [6.50630, 11.91200, 18.99500]
un_filthified = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Un_Filthied.xyz')
un_filthified.cell = [6.50630, 11.91200, 18.99500]
de_pristined.cell = [6.50630, 11.91200, 18.99500]
initialise = [filth, de_filthied, pristine, de_pristined, un_filthified]
initialised = ['Filth', 'De_filthied', 'Pristine', 'De_pristined', 'Un_filthified']

fig, axarr = plt.subplots(5, 4, figsize=(12, 12))
fig.suptitle('Comparison of XYZ Output to Input Files')

for i in range(len(initialise)):
    plot_atoms(initialise[i], axarr[i, 0], radii=0.3, rotation=('0x,0y,0z'))
    plot_atoms(initialise[i], axarr[i, 1], scale=0.7, offset=(3, 4), radii=0.3, rotation=('0x,0y,0z'))
    plot_atoms(initialise[i], axarr[i, 2], radii=0.3, rotation=('45x,45y,0z'))
    plot_atoms(initialise[i], axarr[i, 3], radii=0.3, rotation=('0x,0y,0z'))
    axarr[i, 0].set_title(initialised[i], fontsize=16, color='Red')
    axarr[i, 1].set_xlabel("X-axis, [$\mathrm{\AA}$]")
    axarr[i, 1].set_ylabel("Y-axis, [$\mathrm{\AA}$]")
    axarr[i, 2].set_axis_off()
    axarr[i, 3].set_xlim(0, 6)
    axarr[i, 3].set_ylim(0, 6)

plt.subplots_adjust(hspace=0.6)

fig.savefig("XYZ_Comparisons.png")
plt.show()

# for i in initialise:
#     view(i)