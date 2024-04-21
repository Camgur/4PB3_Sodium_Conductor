from ase.io.cube import read_cube_data
from ase.visualize import view

volumetric_data, atoms = read_cube_data('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Pathways/Optimisation_0_3_bvel.cube')

# print(volumetric_data.shape)
print(atoms)