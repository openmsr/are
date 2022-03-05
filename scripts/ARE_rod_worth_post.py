import matplotlib.pyplot as plt
import openmc
import numpy as np

###############################################################################
#post-processor for rod worth simulation
#reads .txt output from ARE_rod_worth.py
###############################################################################

k_eff_filename = 'k_effs.txt'

shim_rod_positions_converted = [i for i in range(0,36)]
k_effs_simulated = []

# from ORNL-1845, Table J.1, pg. 173
k_effs_experimental = [0.9386,0.9458,0.9523,0.9585,0.9643,0.9695,0.9743,0.9785,
                       0.9825,0.9862,0.9895,0.9926,0.9953,0.9975,0.9992,1.0]

#plot from .txt file
k_file = open('k_effs.txt', 'r')
for k in k_file.readlines():
    k_effs_simulated_thermal_viii.append(float(k))
k_file.close()


plt.plot(shim_rod_positions_converted,k_effs_simulated_scaled_3,linestyle='--',marker='.',label='k_eff simulated')
plt.plot(shim_rod_positions_converted[20:],k_effs_experimental,linestyle='--',marker='.',label='k_eff experimental')
plt.xlabel('Rod position (in.)')
plt.ylabel('k_eff')
plt.legend()
plt.savefig('rod_worth')
