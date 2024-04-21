import os
# Set Graphics Process (MUST BE AT TOP)
os.environ['OVITO_GUI_MODE'] = '1' # Request a session with OpenGL support

from ase.io.cube import read_cube_data
from ase.visualize import view

import math
import pandas as pd
from ovito.io import import_file, export_file
from ovito.modifiers import AssignColorModifier, CoordinationAnalysisModifier, CreateIsosurfaceModifier
from ovito.vis import Viewport, TachyonRenderer


# OVITO:
# https://www.ovito.org/docs/current/python/index.html

# Import Isosurface
volumetric_data, atoms = read_cube_data('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Pathways/Optimisation_0_3_bvel.cube')

print(volumetric_data)

# Import file
pipeline = import_file('/home/camgur/Documents/Coding/Chem_4PB3/Resources/Na4Sn2Ge5O16.cif')
pipeline.add_to_scene()

# Add BVEL to pipeline
def add_bvel(frame, data):
    data.particles_.create_property('BVEL', data=volumetric_data,)
pipeline.modifiers.append(add_bvel)

print(pipeline.compute().grids)
assert 0

# Set up the isosurface modifier:
modifier = CreateIsosurfaceModifier(
    operate_on = 'voxels: VoxelGrid()',
    property = 'BVEL',
    isolevel = 0.4)
pipeline.modifiers.append(modifier)

# Adjust visual appearance of the isosurface in rendered images:
modifier.vis.show_cap = False
modifier.vis.surface_transparency = 0.4



# Enable Viewport
vp = Viewport()
vp = Viewport(type = Viewport.Type.Ortho, camera_dir = (2, 1, -1))
vp.zoom_all()

vp.render_image(size=(1440,2560), filename='/home/camgur/Documents/Coding/Chem_4PB3/Figures/Test.png', background=(0,0,0))



print('Finished!!!')