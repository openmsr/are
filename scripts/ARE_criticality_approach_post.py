import matplotlib.pyplot as plt

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs
filename = 'k_effs.txt'
k_experimental = [0,0.645,0.8010,0.891,0.936,0.962,0.979,0.985,0.989,0.994,0.998,1.00]
runs = [i for i in range(1,13)]

k_simulated = []
stdev_simulated = []

#plot from .txt file
k_file = open(filename, 'r')
for k in k_file.readlines():
    k_eff, std = k.split()
    k_simulated.append(float(k_eff))
    stdev_simulated.append(float(std))
k_file.close()

print(len(k_experimental))
print(len(k_simulated))
# generate plots
fig, ax = plt.subplots()
ax.plot(runs,k_experimental,label = 'experimental',linestyle='--',marker='x')
ax.errorbar(runs,k_simulated, yerr=stdev_simulated,label = 'simulated',linestyle='--',marker='o')
ax.set_xlabel('run no.')
ax.set_ylabel('k')
ax.set_title('ARE criticality approach')
ax.legend()

plt.savefig('criticality_approach.png')
