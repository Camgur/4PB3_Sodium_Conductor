# This code fixes the filthy file to be within the boundary of the unit cell

import pandas as pd
import numpy as np

# Read file
file = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_Fixed.xyz'
filthy_xyz  = pd.read_table(file, skiprows=2, sep='\s+', header=None, index_col=None)

# Convert to nupy array
filthy_xyz = filthy_xyz.to_numpy()

# State boundary conditions
condit = [6.50630, 11.91200, 18.99500]

# Absolute values and boundaries
for i in range(len(filthy_xyz[:, 1])):
    for n in range(1, 4):
        if filthy_xyz[i, n] <= 0.0:
            filthy_xyz[i, n] = np.abs(filthy_xyz[i, n]) + 10e-8
        if filthy_xyz[i, n] >= condit[n-1]:
            filthy_xyz[i, n] = condit[n-1] - 10e-8

# Set header
xyz_shape = np.asarray(filthy_xyz.shape)
xyz_shape = xyz_shape - [0, 1]



# Write to file
filth = open(file='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_filthy.xyz', mode='w')
filth.write(str(xyz_shape[0]))
filth.write('\n')
filth.write('Na4 Sn2 Ge5 O16')
for i in range(len(filthy_xyz[:,0])):
    filth.write('\n')
    filth.write(' '.join(map(str, filthy_xyz[i])))
filth.close()

print('Finished!!!')