from ovito.io import import_file, export_file
from ovito.modifiers import AssignColorModifier, CoordinationAnalysisModifier

# print("Hello world, this is OVITO %i.%i.%i" % ovito.version)

# Set up a new pipeline containing one modifier:
pipeline = import_file('/home/camgur/Documents/Coding/Chem_4PB3/Resources/LiG2_PO4_3.cif')
pipeline.modifiers.append(AssignColorModifier(color = (0.5, 1.0, 0.0)))

# Evaluate the current pipeline a first time:
data1 = pipeline.compute()

# Now altering the pipeline by e.g. changing parameters or appending modifiers:
pipeline.modifiers[0].color = (0.8, 0.8, 1.0)
pipeline.modifiers.append(CoordinationAnalysisModifier(cutoff = 5.0))

# Evaluate the pipeline a second time, now yielding new results:
data2 = pipeline.compute()