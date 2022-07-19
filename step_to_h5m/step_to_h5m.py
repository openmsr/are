###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
import sys
from sys import path
path_to_assembly = os.getcwd() + '/../CAD_to_openMC/src/'
sys.path.append(path_to_assembly)
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_filepath = "./step_files/test_mesh.step"
h5m_out_filepath = os.getcwd() + '/h5m_files/test_mesh_3_50_0.001.h5m'

# mesher config
ab.mesher_config['min_mesh_size'] = 0.001
ab.mesher_config['max_mesh_size'] = 100
ab.mesher_config['curve_samples'] = 50
ab.mesher_config['threads'] = 3
ab.mesher_config['mesh_algorithm'] = 6
#ab.mesher_config['vetoed'] = [474,1157,1243,1341,1537]
#ab.mesher_config['angular_tolerance'] = 0.09

#ab.mesher_config['tolerance'] = 0.001

# output
a=ab.Assembly()
a.verbose=10
a.stp_files=[step_filepath]
a.import_stp_files()
a.solids_to_h5m(backend='gmsh',h5m_filename=h5m_out_filepath)
