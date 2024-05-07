import os
from fuel_salts import *
from build_model import ARE_reactor
import matplotlib.pyplot as plt

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs (nuclear data path is optional)
h5m_files=['h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m']
print(h5m_files)

shim_rod_z = 35.0
ctrl_rod_z = 0.0
run_labels = ( '1','2','3','4','5','6','7','8d','9b','10c','11c','12b' )
crit_run_salts = [ salts[l] for l in run_labels ]

# writes k_eff & stdev separated by a space on each line of the output file
output_filename = 'k_effs_criticality_approach.txt'
with open(output_filename,'w') as k_file:
    print(f'#shim_rod_z={shim_rod_z} in, ctrl_rod_z={ctrl_rod_z} in', file=k_file)
    print('#k_eff k_eff_stddev', file=k_file)

for f in crit_run_salts:
    if f.get_nuclide_densities()['U235'].percent<=0:
      with open(output_filename,'a') as k_file:
        k_file.write('0.0 0.0\n')
    else:
      reactor=ARE_reactor(h5m_files[0],h5m_files[1],h5m_files[2],f,shim_rod_z=[shim_rod_z,shim_rod_z,shim_rod_z],ctrl_rod_z=ctrl_rod_z,batches=5,inactive=1, particles=1000)
      #reactor.bld_model()
      sp_filepath = reactor.model.run(output = True)
      with openmc.StatePoint(sp_filepath) as sp, open(output_filename,'a') as k_file:
        k_eff = sp.keff
        k_file.write(f"{k_eff.nominal_value} {k_eff.std_dev}\n")

# re-read the data-file
k=np.ndarray([len(crit_run_salts),2])
with open(output_filename,'r') as f:
    i=0
    for line in f:
        if line[0]=='#':
            continue
        k[i,:]=line.split()
        i=i+1
print(k)

U235lbs=[concentrations[l][3]/100*concentrations[l][8] for l in run_labels]

f,a = plt.subplots()
a.errorbar(U235lbs, k[:,0], yerr=k[:,1], capsize=3,label=f'shim_rods at {shim_rod_z} in.')
a.set_xlabel('U235 inventory [lbs]')
a.set_ylabel('k_{eff} [ ]')
a.grid()
plt.tight_layout()
plt.legend()
plt.savefig(f'k_eff_vs_U_sz{shim_rod_z}.png')
