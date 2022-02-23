###############################################################################
# Converting step files to h5m file to be read by openmc

# This script uses the following cad_to_h5m version
# https://github.com/LukeLabrie/cad_to_h5m/tree/transforms_and_graveyards
###############################################################################

from cad_to_h5m import cad_to_h5m
import numpy as np

###############################################################################
#inputs
h5m_out_filepath = 'h5m_files/ARE.h5m'
local_cubit_path = "/opt/Coreform-Cubit-2021.5/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))
###############################################################################

cad_to_h5m(h5m_filename= h5m_out_filepath,
            cubit_path=local_cubit_path,
            files_with_tags=[{"material_tag": "inconel",
                             "cad_filename": "step_files/fuel_circuit.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "step_files/pressure_assembly_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "step_files/pressure_assembly_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "step_files/core_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "step_files/thermal_shield_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "BeO",
                             "cad_filename": "step_files/BeO.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_6.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_5.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_4.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_3.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "step_files/ins_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "salt",
                             "cad_filename": "step_files/salt.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "helium",
                             "cad_filename": "step_files/hel_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "coolant",
                             "cad_filename": "step_files/coolant.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "stainless",
                             "cad_filename": "step_files/regulating_rod_0.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "boron",
                             "cad_filename": "step_files/b4c_slugs.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "stainless",
                             "cad_filename": "step_files/shim_rods.step",
                             "transforms":{'scale':scale}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
