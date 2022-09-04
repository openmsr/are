import matplotlib.pyplot as plt
from materials import *
from fuel_salts import *
import openmc
import os

h5m_filepath = os.getcwd() + '/h5m_files/ARE_no_control_rods.h5m'
output_filename = 'k_effs.txt'

def build_model(fuel_comp):

    mats = openmc.Materials([fuel_comp,BeO,inconel,insulation,coolant,helium,stainless,boron])
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

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

k_effs_simulated = []

#writing to text file
k_file = open(output_filename, 'w+')

fuel_comps = [salt2,salt3,salt4,salt5,salt6,salt7,salt8,salt9,salt10,salt11,salt12]

for f in fuel_comps:
    model = build_model(f)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs_simulated.append(k_eff.nominal_value)
        k_file.write("%s\n" %k_eff.nominal_value)

k_file.close()
