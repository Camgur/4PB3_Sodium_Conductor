from ase import atoms, units
from ase.io import read, write
from ase.visualize import view
from ase.io.trajectory import Trajectory

from mace.calculators import MACECalculator

# Import Trajectories
traj = []
for i in range(15):
    traject = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Trajectories/Trajectory_1_' + str(i) + '.traj'
    traj.append(Trajectory(traject))

# Draft Compiled Trajectory
write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled_traj.traj', '')
for i in range(len(traj[0])):
    atom = None
    atoms = []
    for n in range(len(traj)):
        atoms.append(traj[n][i])
    atom = atoms[0] + atoms[1] + atoms[2] + atoms[3] + atoms[4] + atoms[5] + atoms[6] + atoms[7] +\
            atoms[8] + atoms[9] + atoms[10] + atoms[11] + atoms[12] + atoms[13] + atoms[14]
    with Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled_traj.traj', mode='a') as trajectory:
        trajectory.write(atom)

traj = Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled_traj.traj')

for i in range(len(traj)):
    atoms = traj[i]
    write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Gif_CIFs/Compiled_' + str(i) + '.xyz', atoms)


write('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled.traj', '')
for i in range(160):
    atoms = read('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Gif_CIFs/Compiled_' + str(i) + '.xyz')
    with Trajectory('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Compiled.traj', mode='a') as traje:
        traje.write(atoms)