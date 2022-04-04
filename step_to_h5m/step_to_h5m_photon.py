###############################################################################
# Converting step files to h5m file to be read by openmc

# Creates h5m file from step files for each rod position

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/material_tag


# Includes parts for measuring gamma spectra
###############################################################################


from cad_to_h5m import cad_to_h5m
import numpy as np
import os

expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

cad_to_h5m(h5m_filename= os.getcwd()  + '/h5m_files/ARE_gamma.h5m',
            cubit_path="/opt/Coreform-Cubit-2021.11/bin/",
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
                            {"material_tag": "blanket",
                             "cad_filename": "step_files/blanket.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "iron",
                             "cad_filename": "step_files/shield.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "air",
                             "cad_filename": "step_files/filter.step",
                             "transforms":{'scale':scale}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
