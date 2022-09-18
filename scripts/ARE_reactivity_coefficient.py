import os
from build_model import build_model

###############################################################################
# crude temperature reactivity coefficient estimate
###############################################################################

# inputs (nuclear data path is optional)
h5m_filepath = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
nuclear_data_path = None
output_filename = 'coefficients.txt'

# started at 1312F = (1312F-32 F)*5/9 --> 711.1111 C
# experiement was from 1150 to 1312
temps = [(i-32)*5/9 for i in range(1150,1313)]
k_effs = []

results = open(output_filename,'w+')
for t in temps:
    model = build_model(h5m_filepath,operating_temp=t)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs.append(k_eff.nominal_value)
        results.write(f"{k_eff.nominal_value}\n")

coeffs = [(k_effs[i]-k_effs[i-1])/k_effs[i] for i in range(1,len(k_effs))]
results.write(f'temperature coefficient of reactivity estimate: {mean(coeffs)}')
