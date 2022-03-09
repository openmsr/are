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
            cubit_path="/opt/Coreform-Cubit-2021.5/bin/",
            files_with_tags=[{"material_tag": "inconel",
                             "cad_filename": "reactor_parts_photon/fuel_circuit.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts_photon/pressure_assembly_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts_photon/pressure_assembly_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts_photon/core_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "inconel",
                             "cad_filename": "reactor_parts_photon/thermal_shield_metal.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "BeO",
                             "cad_filename": "reactor_parts_photon/BeO.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_6.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_5.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_4.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_3.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "insulation",
                             "cad_filename": "reactor_parts_photon/ins_1.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "salt",
                             "cad_filename": "reactor_parts_photon/salt.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "helium",
                             "cad_filename": "reactor_parts_photon/hel_2.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "coolant",
                             "cad_filename": "reactor_parts_photon/coolant.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "stainless",
                             "cad_filename": "reactor_parts_photon/regulating_rod_0.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "boron",
                             "cad_filename": "reactor_parts_photon/b4c_slugs.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "stainless",
                             "cad_filename": "reactor_parts_photon/shim_rods.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "blanket",
                             "cad_filename": "reactor_parts_photon/blanket.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "iron",
                             "cad_filename": "reactor_parts_photon/shield.step",
                             "transforms":{'scale':scale}},
                            {"material_tag": "air",
                             "cad_filename": "reactor_parts_photon/filter.step",
                             "transforms":{'scale':scale}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
