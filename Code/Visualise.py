import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase.visualize import view
import seaborn as sns
import numpy as np

# From: https://wiki.fysik.dtu.dk/ase/ase/visualize/visualize.html

# Set import and add atoms
de_filthied = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Bad/De_Filthied.xyz', '0')
filth = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_filthy.xyz', '0')
pristine = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16.xyz', '0')
fixed = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_Fixed.xyz', '0')
de_pristined = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Bad/De_Pristined.xyz', '0')
un_filthified = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Bad/Un_Filthied.xyz', '0')
re_fixed = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Re_fixed.xyz', '0')

# Set vectors
initialise = [filth, fixed, pristine, de_filthied, de_pristined, un_filthified]
initialised = ['Filth', 'Fixed_pristine', 'Pristine', 'De_filthied', 'De_pristined', 'Un_filthified', 'Re_fixed']

# Begin Plot
fig, axarr = plt.subplots(6, 4, figsize=(20, 20))
fig.suptitle('Comparison of XYZ Output to Input Files')

for i in range(len(initialise)):
    initialise[i].cell = [6.50630, 11.91200, 18.99500]
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

fig.savefig("/home/camgur/Documents/Coding/Chem_4PB3/XYZ_Comparisons.png")
# plt.show()

# for i in initialise:
#     view(i)