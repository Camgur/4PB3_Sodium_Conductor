import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase.visualize import view

# From: https://wiki.fysik.dtu.dk/ase/ase/visualize/visualize.html

# Set atoms
atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16.xyz', '0')
de_pristined = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/De_Pristined.xyz', '0')

# view(atoms)

# fig, axarr = plt.subplots(1, 4, figsize=(15, 5))
# plot_atoms(atoms, axarr[0], radii=0.3, rotation=('0x,0y,0z'))
# plot_atoms(atoms, axarr[1], scale=0.7, offset=(3, 4), radii=0.3, rotation=('0x,0y,0z'))
# plot_atoms(atoms, axarr[2], radii=0.3, rotation=('45x,45y,0z'))
# plot_atoms(atoms, axarr[3], radii=0.3, rotation=('0x,0y,0z'))
# axarr[0].set_title("No rotation")
# axarr[1].set_xlabel("X-axis, [$\mathrm{\AA}$]")
# axarr[1].set_ylabel("Y-axis, [$\mathrm{\AA}$]")
# axarr[2].set_axis_off()
# axarr[3].set_xlim(2, 6)
# axarr[3].set_ylim(2, 6)
# fig.savefig("ase_slab_multiple.png")

view(atoms)
view(de_pristined)