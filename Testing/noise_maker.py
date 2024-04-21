import pandas as pd
import numpy as np

'''
# This code has issues (something to do with the file on github)
inputfile = 'https://github.com/Camgur/4PB3_Sodium_Conductor/blob/891ffd70d43345ba22855ba44c80ce239b0b8bc7/xyz/Na4Sn2Ge5O16.xyz'
df  = pd.read_table(inputfile, skiprows=2, sep='\s+', names=['atom', 'x', 'y', 'z'])
print(df.head(4))
'''


# Read file
file = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_Fixed.xyz'
clean_xyz  = pd.read_table(file, skiprows=2, sep='\s+', header=None, index_col=None)

# Convert to nupy array
clean_xyz = clean_xyz.to_numpy()



# Find gaussian noise shape
xyz_shape = np.asarray(clean_xyz.shape)
xyz_shape = xyz_shape - [0, 1]

# Generate gaussian noise
gauss_noise = np.random.normal(10e-8, 10e-8, (xyz_shape))

# Add noise to xyz
filthy_xyz = clean_xyz
for i in range(3):
    filthy_xyz[:,i+1] = clean_xyz[:,i+1] + gauss_noise[:,i]



# Write new file
filth = open(file='/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16_filthy.xyz', mode='w')
filth.write(str(xyz_shape[0]))
filth.write('\n')
filth.write('Na4 Sn2 Ge5 O16')
for i in range(len(filthy_xyz[:,0])):
    filth.write('\n')
    filth.write(' '.join(map(str, filthy_xyz[i])))
filth.close()

print('Finished!!!')