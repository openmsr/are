###############################################################################
# Converting step files to h5m file to be read by openmc

# Creates h5m file from step files for each rod position

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/material_tag
###############################################################################

from cad_to_h5m import cad_to_h5m
import numpy as np
import os

###############################################################################
#inputs
h5m_out_filepath = os.getcwd() + '/h5m_files/rod_worth/ARE'
local_cubit_path = "/opt/Coreform-Cubit-2021.5/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))
rod_pos = np.linspace(0,90,36)
###############################################################################

#generating an h5m file for each rod position
for pos in rod_pos:
    cad_to_h5m(h5m_filename = h5m_out_filepath + '_pos_' + str(pos)[0:2]+ '.h5m',
            cubit_path=local_cubit_path,
            files_with_tags=[{"material_tag": "inconel",
                             "cad_filename": "reactor_parts/fuel_circuit.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts/pressure_assembly_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts/pressure_assembly_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts/core_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts/thermal_shield_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "BeO",
                             "cad_filename": "reactor_parts/BeO.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_6.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_5.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_4.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_3.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts/ins_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "salt",
                             "cad_filename": "reactor_parts/salt.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "helium",
                             "cad_filename": "reactor_parts/hel_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "coolant",
                             "cad_filename": "reactor_parts/coolant.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "stainless",
                             "cad_filename": "reactor_parts/regulating_rod_0.step",
                             "transforms":{'scale':scale,'move':[0,0,pos]}},
                            {"material_tag": "boron",
                             "cad_filename": "reactor_parts/b4c_slugs.step",
                             "transforms":{'scale':scale,'move':[0,0,pos]}},
                            {"material_tag": "stainless",
                             "cad_filename": "reactor_parts/shim_rods.step",
                             "transforms":{'scale':scale,'move':[0,0,pos]}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
