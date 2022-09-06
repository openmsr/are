import os
from fuel_salts import *
from build_model import build_model

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs
filename = 'k_effs.txt'
k_experimental = [0,0.645,0.8010,0.891,0.936,0.962,0.979,0.985,0.989,0.994,0.998,1.00]
runs = [i for in in range(1,13)]

k_simulated = [0]
stdev_simulated = [0]

#plot from .txt file
k_file = open('k_effs.txt', 'r')
for k in k_file.readlines():
    k_eff, std = k.split()
    k_simulated.append(float(k_eff))
    stdev_simulated.append(float(std))
k_file.close()

# generate plots
fig, ax = plt.subplots()
ax.plot(runs,k_experimental,label = 'experimental',linestyle='--',marker='x')
ax_m.errorbar(runs,k_simulated, yerr=stdev_simulated,label = 'simulated',linestyle='--',marker='o')
ax_m.set_xlabel('run no.')
ax_m.set_ylabel('k')
ax_m.set_title('ARE criticality approach')
ax_m.legend()

plt.show()
