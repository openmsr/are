###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
import sys
sys.path.append('../CAD_to_openMC/src/')
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_filepath = "./step_files/are.step"
h5m_out_filepath = os.getcwd() + '/h5m_files/are.h5m'

# mesher config
ab.mesher_config['min_mesh_size'] = 0.5
ab.mesher_config['min_mesh_size'] = 100
ab.mesher_config['mesh_algorithm'] = 1
ab.mesher_config['threads'] = 56
ab.mesher_config['curve_samples'] = 100

ab.mesher_config['refine'] = 0
# output
a=ab.Assembly([step_filepath],verbose=2)
a.run(backend='stl',h5m_filename=h5m_out_filepath)
