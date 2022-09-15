import os
from fuel_salts import *
from build_model import build_model

###############################################################################
# crude temperature reactivity coefficient estimate
###############################################################################

# inputs (nuclear data path is optional)
h5m_filepath = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
nuclear_data_path = None

# started at 1312F = (1312F-32 F)*5/9 --> 711.1111 C
# experiement was from 1150 to 1312
temps = [(i-32)*5/9 for i in range(1150,1313)]
k_effs = []

# writes k_eff & stdev separated by a space on each line of the output file
for t in temps:
    model = build_model(f,h5m_filepath,nuclear_data_path,t)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs.append(k_eff.nominal_value)

coeffs = [(k_effs[i]-k_effs[i-1])/k_effs[i] for i in range(1,len(k_effs))]
print(f'temperature coefficient of reactivity estimate: {mean(coeffs)}')
