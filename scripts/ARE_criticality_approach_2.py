import os
from fuel_salts import *
from build_model import build_model
from make_salt import make_fuel

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs (nuclear data path is optional)
h5m_filepath = os.getcwd() + '/h5m_files/ARE_rods_35.h5m'
operating_temp = 977.59
density_are = 3.3142201
output_filename = 'k_effs.txt'
nuclear_data_path = None

# fuel compositions; calculated via weight added on ORNL-1845 pg. 43
na_wp = [10.99,11.01,11.03,11.05,11.06,11.08,11.09,11.10,11.11,11.12,11.12,11.13]
zr_wp = [42.24,41.14,39.86,38.72,37.62,36.62,36.02,35.7,35.25,34.82,34.52]
u235_wp = [1.74,3.14,4.73,6.22,7.62,8.90,9.66,10.07,10.64,11.18,11.57]
u238_wp = [0.12,0.22,0.34,0.45,0.55,0.64,0.69,0.72,0.76,0.80,0.83]
f_wp = [44.89,44.47,44.00,43.55,43.14,42.75,42.53,42.40,42.23,42.07,41.96]
densities = [3.114,3.140,3.176,3.207,3.234,3.260,3.276,3.284,3.295,3.306,3.314]

# fuel
fuel_comps = []
for i in range(len(na_wp)):
    s = make_fuel(na=na_wp[i],
                  zr=zr_wp[i],
                  f=f_wp[i],
                  u235=u235_wp[i],
                  u238=u238_wp[i],
                  temp=operating_temp,
                  density=densities[i],
                  enriched=93.4)
    fuel_comps.append(s)

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
