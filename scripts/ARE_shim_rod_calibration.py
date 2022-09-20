import os
from build_model import build_model
import openmc
from fuel_salts import salt_8A,salt_9B,salt_10C,salt_11C,salt_12B

###############################################################################
# shim rod calibration data comparison
###############################################################################

# inputs (nuclear data path is optional)
pos_20 = os.getcwd() + '/h5m_files/ARE_rods_20.h5m'
pos_25 = os.getcwd() + '/h5m_files/ARE_rods_25.h5m'
pos_30 = os.getcwd() + '/h5m_files/ARE_rods_30.h5m'
pos_35 = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
positions = [pos_20,pos_25,pos_30,pos_35]

nuclear_data_path = None
output_filename = 'k_effs_calibration.txt'

salts = [salt_8A,salt_9B,salt_10C,salt_11C,salt_12B]

# store set of k_effs for each fuel concentration
k_effs = []

# calibration was run against 14 different fuel concentrations
# loop through each fuel concentrations
# loop through each position
for s in salts:
    k_pos = []
    for p in positions:
        model = build_model(p,fuel=s)
        sp_filepath = model.run(output = True)

        with openmc.StatePoint(sp_filepath) as sp:
            k_eff = sp.k_combined
            k_pos.append(k_eff.nominal_value)
    k_effs.append(k_pos)

results = open(output_filename,'w+')
for l in k_effs:
    for i in l:
        results.write(f"{i} ")
    results.write("\n")
results.close()
