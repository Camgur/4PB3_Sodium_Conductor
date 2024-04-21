from ase import atoms, units
from ase.io import read, write
from ase.visualize import view
from ase.io.trajectory import Trajectory
import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms

from mace.calculators import MACECalculator

# traj = Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled_traj.traj')
test = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled.traj')
# print(test)

# RUNNING into issues
# write('/home/camgur/Documents/Coding/Chem_4PB3/Movies/Unit_cell_opt.png', traj[0], radii=0.7)

# print(traj[0].get_positions().shape)
# print(len(traj))

view(test)

# traj = []
# for i in range(15):
#     traject = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Trajectories/Trajectory_1_' + str(i) + '.traj'
#     traj.append(Trajectory(traject))

# fig, axarr = plt.subplots(1, 4, figsize=(14, 12))
# fig.suptitle('Comparison of Files')

# for i in range(1):
#     plot_atoms(test, axarr[0], radii=0.1, rotation=('0x,0y,0z'))
#     plot_atoms(test, axarr[1], scale=0.7, offset=(3, 4), radii=0.1, rotation=('0x,0y,0z'))
#     plot_atoms(test, axarr[2], radii=0.1, rotation=('45x,45y,0z'))
#     plot_atoms(test, axarr[3], radii=0.1, rotation=('0x,0y,0z'))
#     axarr[0].set_title('Placeholder', fontsize=16, color='Red')
#     axarr[1].set_xlabel("X-axis, [$\mathrm{\AA}$]")
#     axarr[1].set_ylabel("Y-axis, [$\mathrm{\AA}$]")
#     axarr[2].set_axis_off()
#     axarr[3].set_xlim(0, 6)
#     axarr[3].set_ylim(0, 6)

# plt.subplots_adjust(hspace=0.6)

# # # fig.savefig("/home/camgur/Documents/Coding/Chem_4PB3/Movies/Unit_cell_opt.png")
# plt.show()