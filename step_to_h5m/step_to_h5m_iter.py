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
step_filepath = "./step_files/ARE_2.step"

iters = 2000
i = 0
# mesher config
ab.mesher_config['min_mesh_size'] = 0.001
ab.mesher_config['max_mesh_size'] = 100
ab.mesher_config['curve_samples'] = 50
ab.mesher_config['threads'] = 55
ab.mesher_config['mesh_algorithm'] = 2
ab.mesher_config['vetoed'] = [1157,1159,1243,1341,1537]
while i<iters:
    h5m_out_filepath = os.getcwd() + '/h5m_files/ARE_try_' + str(i) + '.h5m'
    # output
    try:
        a=ab.Assembly()
        a.verbose=10
        a.stp_files=[step_filepath]
        a.import_stp_files()
        a.solids_to_h5m(backend='gmsh',h5m_filename=h5m_out_filepath)
    except:
        ab.mesher_config['min_mesh_size'] += 0.001
    i += 1



#ab.mesher_config['angular_tolerance'] = 0.09

#ab.mesher_config['tolerance'] = 0.001
