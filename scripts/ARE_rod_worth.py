import openmc
import numpy as np
from materials import *

###############################################################################
# rod worth simulation of ARE

# exports a .txt file with a k_eff at each position

# 0in. withdrawn - 36in. withdrawn (full) at one inch increments
###############################################################################

output_filename = 'k_effs.txt'

#equilibrium operating temperature in kelvin
operating_temp = 977.5944

def build_model(dagmc_file):

    mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron])
    mats.export_to_xml()

    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = 100
    settings.inactive = 10
    settings.particles = 10000
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(dagmc_file)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

shim_rod_positions = np.linspace(0,36,36)
h5m_filenames = ['h5m_files/rod_worth/ARE_pos_' + str(i)[0:2] + '.h5m' for i in shim_rod_positions]
k_effs_simulated = []

#writing to text file
k_file = open(output_filename, 'w+')

for filename in h5m_filenames:
    model = build_model(filename)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs_simulated.append(k_eff.nominal_value)
        k_file.write("%s\n" %k_eff.nominal_value)

k_file.close()
