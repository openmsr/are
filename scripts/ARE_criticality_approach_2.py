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
na_wp = [11.25,11.45,11.71,11.96,12.20,12.42,12.47,12.57,12.64,12.76,12.86,12.93]
zr_wp = [43.22,42.90,42.53,42.16,41.81,41.65,41.40,41.26,41.14,40.98,40.82,40.71]
u_wp = [1.82,3.34,5.13,6.89,8.60,10.23,10.53,11.23,11.77,12.54,13.29,13.83]
f_wp = [43.71,42.30,40.63,38.99,37.40,35.88,35.59,34.95,34.44,33.72,33.02,32.52]

# fuel
fuel_comps = []
for i in range(len(na_wp)):
    s = make_fuel(na=na_wp[i],
                  zr=zr_wp[i],
                  f=f_wp[i],
                  u=u_wp[i],
                  temp=operating_temp,
                  density=density_are,
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
