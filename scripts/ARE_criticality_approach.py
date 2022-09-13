import os
from fuel_salts import *
from build_model import build_model

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs
h5m_filepath = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
fuel_comps = [salt2,salt3,salt4,salt5,salt6,salt7,salt8,salt9,salt10,salt11,salt12]
output_filename = 'k_effs_jeff33_reg.txt'

# experimental values
runs = [i for i in range(1,13)]

# writes k_eff & stdev separated by a space on each line of the output file
k_file = open(output_filename,'w+')
for f in fuel_comps:
    model = build_model(f,h5m_filepath,'/home/luke/openmc/nuclear_data/jeff33_hdf5/cross_sections.xml')
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_file.write(f"{k_eff.nominal_value} {k_eff.std_dev}\n")
k_file.close()
