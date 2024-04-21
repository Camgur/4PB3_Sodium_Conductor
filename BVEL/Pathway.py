from bvlain import Lain

'''
!!!
PyPI link (diffpy.srreal):
https://pypi.org/project/diffpy.srreal/
https://github.com/diffpy/diffpy.srreal/

User Manual:
https://www.diffpy.org/diffpy.srreal/

Alternate Library (PyAbstantia):
https://shinichinishimura.github.io/pyabst/
!!!
'''

# Actually Using: BVlain
# https://pypi.org/project/bvlain/
# https://bvlain.readthedocs.io/en/latest/index.html

# Initialise File
file = '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation_Stuff/Optimisation_0_3.cif'
# Set Calculator
calc = Lain(verbose=True)
# Set State
st = calc.read_file(file)

params = {'mobile_ion': 'Na1+',    # mobile specie
		  'r_cut': 10.0,           # cutoff for interaction between the mobile species and framework
		  'resolution': 0.01,	   # distance between the grid points
		  'k': 150                 # maximum number of neighbors to be collected for each point
}

# Run Distributions
_ = calc.bvse_distribution(**params)
# _ = calc.void_distribution(**params)

# print(_)
# assert 0

# Perform Percolation Analysis
calc.percolation_barriers(encut = 5.0)

# Create Savestate
savestate = file.replace('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Optimisation_Stuff/', '/home/camgur/Documents/Coding/Chem_4PB3/Resources/Pathways/').replace('.cif', '_bvel')
# print(savestate)
# assert 0

# Write Grid File
calc.write_grd(filename = savestate, task = 'bvse')  # saves .grd file
calc.write_cube(filename = savestate, data = _)  # saves .cube file

# Check for Mismatches
table = calc.mismatch(r_cut = 4.0)
# print(table.to_string())
print('Finished!!!')


# MAKE SURE TO SET ISOSURFACE TO 0.4
# MUST SET THE ISOSURFACE TO NEGATIVE