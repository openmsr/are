###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
from sys import path

###############################################################################
#inputs

# get assembly module
path_to_assembly = os.getcwd() + '/../step_to_h5m/src/h5massembly'
path.append(path_to_assembly)
import assembly as ab

h5m_out_filepath = os.getcwd() + '/h5m_files/ARE.h5m'

a=ab.Assembly()
a.stp_files=[os.getcwd()+"/step_files/ARE.step"]
a.import_stp_files()
a.export_brep('ARE.brep')
a.brep_to_h5m(brep_filename='ARE.brep',
              h5m_filename='ARE.h5m',
              threads=55)
