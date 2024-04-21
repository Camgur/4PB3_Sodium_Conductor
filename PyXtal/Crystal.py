from pyxtal import pyxtal
from pyxtal.symmetry import Group
from pyxtal.io import write_cif

'''
Symmetry with ASE:
https://github.com/ajjackson/ase-tutorial-symmetry/blob/master/ase-symmetry.md

PyXtal Documentation:
https://pyxtal.readthedocs.io/en/latest/

'''


for i in range(5):
    crystal = pyxtal()
    crystal.from_random(dim=3, group=60, species=['Ge', 'Na', 'O', 'Sn'], numIons=[20,16,64,8], lattice=[6.5063, 11.912, 18.995])
    print(crystal)
    filename = 'Chem_4PB3/Resources/Sample_Crystals/Sample_'
    filename += str(i)
    filename += '.cif'
    write_cif(crystal, filename=filename, permission='w', style='icsd')