import os
from fuel_salts import *
from build_model import build_model
import matplotlib.pyplot as plt

###############################################################################
# ARE shim rod calibration experiment
###############################################################################
import os

# inputs
filename ='k_effs_calibration.txt'
s8A_experimental = [0.860,0.883,0.904,0.918]
s9B_experimental = [0.889,0.919,0.942,0.952]
s10C_experimental = [0.913,0.934,0.960,0.972]
s11C_experimental = [0.925,0.952,0.977,0.990]
s12B_experimental = [0.935,0.967,0.988,1.00]

# simulated
simulated = []

# read endfb80 data
k_file = open(filename, 'r')
for k in k_file.readlines():
    k_effs = k.split()
    simulated.append([float(k) for k in k_effs])
k_file.close()

# generate plot
pos = [20,25,30,35]
fig, ax = plt.subplots()
ax.plot(pos,s8A_experimental,label = '8A: experimental',linestyle='--',marker='x')
ax.plot(pos,s9B_experimental,label = '9B: experimental',linestyle='--',marker='x')
ax.plot(pos,s10C_experimental,label = '10C: experimental',linestyle='--',marker='x')
ax.plot(pos,s11C_experimental,label = '11C: experimental',linestyle='--',marker='x')
ax.plot(pos,s12B_experimental,label = '12B: experimental',linestyle='--',marker='x')

ax.plot(pos,simulated[0],label = '8A: simulated',linestyle='--',marker='x')
ax.plot(pos,simulated[1],label = '9B: simulated',linestyle='--',marker='x')
ax.plot(pos,simulated[2],label = '10C: simulated',linestyle='--',marker='x')
ax.plot(pos,simulated[3],label = '11C: simulated',linestyle='--',marker='x')
ax.plot(pos,simulated[4],label = '12B: simulated',linestyle='--',marker='x')

ax.set_xlabel('control rod pos (in. withdrawn)')
ax.set_ylabel('k')
ax.set_title('ARE shim rod calibration')
ax.legend()

plt.show()
