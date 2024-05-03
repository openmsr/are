import matplotlib.pyplot as plt

###############################################################################
# ARE criticality approach experiment
###############################################################################

# inputs
filename = 'k_effs.txt'
k_experimental = [0,0.645,0.8010,0.891,0.936,0.962,0.979,0.985,0.989,0.994,0.998,1.00]
runs = [i for i in range(1,13)]

k_simulated = [0]
stdev_simulated = [0]

#plot from .txt file
k_file = open(filename, 'r')
for k in k_file.readlines():
    k_eff, std = k.split()
    k_simulated.append(float(k_eff))
    stdev_simulated.append(float(std))
k_file.close()

# generate plots
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(runs, k_experimental, label='ORNL-1845', color='forestgreen', linestyle='-', marker='o')
ax.plot(runs, k_simulated, label='OpenMC', color='indianred', linestyle='-', marker='x')
ax.set_xlabel('Run Number', fontsize=14)
ax.set_ylabel('k', fontsize=14)
ax.set_title('ARE Criticality Approach', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True)
plt.savefig('criticality_approach.png')
plt.show()
