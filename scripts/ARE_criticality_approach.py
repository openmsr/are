import os
from fuel_salts import *
from build_model import build_model

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs (nuclear data path is optional)
h5m_filepath = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
fuel_comps = [salt2,salt3,salt4,salt5,salt6,salt7,salt8,salt9,salt10,salt11,salt12]
output_filename = 'k_effs.txt'
nuclear_data_path = None

# experimental values
runs = [i for i in range(1,13)]

# writes k_eff & stdev separated by a space on each line of the output file
k_file = open(output_filename,'w+')
for f in fuel_comps:
    model = build_model(h5m_filepath,f,nuclear_data_path)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_file.write(f"{k_eff.nominal_value} {k_eff.std_dev}\n")
k_file.close()
