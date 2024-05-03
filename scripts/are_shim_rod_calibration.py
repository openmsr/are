import os
from fuel_salts import *
from build_model import ARE_reactor

import matplotlib.pyplot as plt

###############################################################################
# ARE Shim rod calibration data comparison
###############################################################################

# inputs (nuclear data path is optional)
h5m_files = [os.getenv('HOME') + '/Sandbox/are/' + f for f in ['ARE_b_salt_beo_cool_v9.h5m','ARE_safety_rod.h5m','ARE_regulating_rod.h5m']]
print(h5m_files)

operating_temp = 977.59
density_are = 3.3142201
shim_rod_z=35.0
ctrl_rod_z=0.0

run_labels = ['8a','8d','9a','9b','10a','10b','10c','11a','11b','11c','12a','12b']
shim_rod_salts={l:salts[l] for l in run_labels}

positions=[20,25,30,35]

# calibration was run against 14 different fuel concentrations
# loop through each fuel concentrations# loop through each position
output_filename='k_effs_shim_rod_calibration.dat'
for l,s in shim_rod_salts.items():
    U235lbs=concentrations[l][8]*concentrations[l][3]/100.0
    for sz in positions:
      reactor=ARE_reactor(h5m_files[0],h5m_files[1],h5m_files[2],s,shim_rod_z=[sz,sz,sz],ctrl_rod_z=ctrl_rod_z,batches=200,inactive=5, particles=200)
      reactor.bld_model()
      reactor.export_to_xml()

      sp_filepath = reactor.model.run(output = True)
      with openmc.StatePoint(sp_filepath) as sp, open(output_filename,'a') as k_file:
        k_eff = sp.keff
        k_file.write(f'{l} {U235lbs} {sz} {k_eff.nominal_value} {k_eff.std_dev}\n')

# post processing
filename ='k_effs_calibration.txt'
s8A_experimental = [0.860,0.883,0.904,0.918]
s9B_experimental = [0.889,0.919,0.942,0.952]
s10C_experimental = [0.913,0.934,0.960,0.972]
s11C_experimental = [0.925,0.952,0.977,0.990]
s12B_experimental = [0.935,0.967,0.988,1.00]

# simulated
simulated = []

with open(filename, 'r') as k_file:
    for k in k_file.readlines():
        k_effs = k.split()
        simulated.append([float(k) for k in k_effs])

# generate plot
pos = [20,25,30,35]

fig, ax = plt.subplots()
ax.plot(pos,s8A_experimental,label = '8A: experimental',linestyle='--',marker='x')
ax.plot(pos,s9B_experimental,label = '9B: experimental',linestyle='--',marker='x')
ax.plot(pos,s10C_experimental,label = '10C: experimental',linestyle='--',marker='x')
ax.plot(pos,s11C_experimental,label = '11C: experimental',linestyle='--',marker='x')
ax.plot(pos,s12B_experimental,label = '12B: experimental',linestyle='--',marker='x')

ax.errorbar(pos,simulated[0],label = '8A: simulated',linestyle='--',marker='x')
ax.errorbar(pos,simulated[1],label = '9B: simulated',linestyle='--',marker='x')
ax.errorbar(pos,simulated[2],label = '10C: simulated',linestyle='--',marker='x')
ax.errorbar(pos,simulated[3],label = '11C: simulated',linestyle='--',marker='x')
ax.errorbar(pos,simulated[4],label = '12B: simulated',linestyle='--',marker='x')

ax.set_xlabel('shim rod position [in]')
ax.set_ylabel('k [ ]')
ax.set_title('ARE shim rod calibration')
ax.legend()

plt.savefig('k_vs_shim_rod_pos.png')
