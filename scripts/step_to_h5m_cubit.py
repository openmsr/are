
###############################################################################
# Converting step files to h5m file to be read by openmc

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/material_tag
###############################################################################

from cad_to_h5m import *
import numpy as np
import os

###############################################################################
#inputs
step_filepath = os.getcwd()  + '/step_files/are_rods_35.step'
h5m_out_filepath = os.getcwd()  + '/h5m_files/ARE_rods_35.h5m'
local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))
###############################################################################

cad_to_h5m(h5m_filename= h5m_out_filepath,
            cubit_path=local_cubit_path,
            files_with_tags=[{"cad_filename": step_filepath,
                             "transforms":{'scale':scale}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )