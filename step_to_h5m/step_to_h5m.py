###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
from sys import path
path_to_assembly = os.getcwd() + '/../CAD_to_OpenMC/'
sys.path.append(path_to_assembly)
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_filepath = "./step_files/ARE.step"
h5m_out_filepath = os.getcwd() + '/h5m_files/ARE.h5m'

a=ab.Assembly()
a.verbose=10
a.stp_files=[step_filepath]
a.import_stp_files()
a.solids_to_h5m(backend='stl',h5m_filename=h5m_out_filepath,threads=6)
