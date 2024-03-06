from ase.io import read
import numpy as np
from mace.calculators import MACECalculator

calculator = MACECalculator(model_paths='/home/camgur/Documents/Coding/Chem_4PB3/Resources/2024-01-07-mace-128-L2_epoch-199.model', device='cuda')
init_conf = read('/home/camgur/Documents/Coding/Chem_4PB3/Na4Sn2Ge5O16_filthy.xyz', '0')


descriptors = calculator.get_descriptors(init_conf)