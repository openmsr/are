import os
from fuel_salts import *
from build_model import ARE_reactor
#from make_salt import make_are_fuel

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs (nuclear data path is optional)
h5m_files = [os.getenv('HOME') + '/Sandbox/are/' + f for f in ['ARE_b_salt_beo_cool_v9.h5m','ARE_safety_rod.h5m','ARE_regulating_rod.h5m']]
print(h5m_files)

operating_temp = 977.59
density_are = 3.3142201
shim_rod_z=35.0
ctrl_rod_z=0.0

#no Hf in this
crit_run_salts=[salts['1'],salts['2'],salts['3'],salts['4'],salts['5'],
	salts['6'],salts['7'],salts['8d'],salts['9b'],salts['10c'],salts['11c'],salts['12a']]

# writes k_eff & stdev separated by a space on each line of the output file
output_filename='k_effs_criticality_approach.txt'
with open(output_filename,'a') as k_file:
    print(f'#shim_rod_z={shim_rod_z} in, ctrl_rod_z={ctrl_rod_z} in', file=k_file)
    print('#k_eff k_eff_stddev', file=k_file)

for f in crit_run_salts:
    if f.get_nuclide_densities()['U235'].percent<=0:
      with open(output_filename,'a') as k_file:
        k_file.write('0.0 0.0\n')
    else:
      reactor=ARE_reactor(h5m_files[0],h5m_files[1],h5m_files[2],f,shim_rod_z=[shim_rod_z,shim_rod_z,shim_rod_z],ctrl_rod_z=ctrl_rod_z,batches=200,inactive=5, particles=10000)
      reactor.bld_model()
      reactor.bld_plots()
      reactor.plots.export_to_xml()
      reactor.export_to_xml()
      sp_filepath = reactor.model.run(output = True)
      with openmc.StatePoint(sp_filepath) as sp, open(output_filename,'a') as k_file:
        k_eff = sp.keff
        k_file.write(f"{k_eff.nominal_value} {k_eff.std_dev}\n")
