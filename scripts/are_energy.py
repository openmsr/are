import openmc
import matplotlib.pyplot as plt
import numpy as np

from build_model import ARE_reactor

###############################################################################
#create .png files of photon flux (all safety rods inserted)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m', particles=1000)

#tallies
tallies = openmc.Tallies()

# particle filters
neutron_particle_filter=openmc.ParticleFilter(['neutron'])
photon_particle_filter=openmc.ParticleFilter(['photon'])

# energy binned filters
energy_bins = openmc.mgxs.GROUP_STRUCTURES['VITAMIN-J-175']
energy_filter = openmc.EnergyFilter(energy_bins)

# tallies
tallyEn = openmc.Tally(name='energyn')
tallyEn.filters = [energy_filter,neutron_particle_filter]
tallyEn.scores = ['flux']
tallies.append(tallyEn)

tallyEp = openmc.Tally(name='energyp')
tallyEp.filters = [energy_filter,photon_particle_filter]
tallyEp.scores = ['flux']
tallies.append(tallyEp)

ARE.bld_model()
ARE.model.tallies=tallies
ARE.model.settings.photon_transport=True

sp_filename = ARE.model.run()
sp = openmc.StatePoint(sp_filename)

n_tally = sp.get_tally(name='energyn')
p_tally = sp.get_tally(name='energyp')

fluxn = n_tally.get_slice(scores=['flux'])
fluxp = p_tally.get_slice(scores=['flux'])

fig,ax = plt.subplots()
energy_midpts=(energy_bins[:-1]+energy_bins[1:])*0.5
pos=ax.errorbar(energy_midpts,fluxn.mean.squeeze(), yerr=fluxn.std_dev.squeeze(), capsize=3, capthick=1, label='neutron flux')
pos=ax.errorbar(energy_midpts,fluxp.mean.squeeze(), yerr=fluxp.std_dev.squeeze(), capsize=3, capthick=1, label='photon flux')
ax.grid()
ax.set_xscale('log')
ax.set_xlabel('energy [eV]')
ax.set_ylabel('flux [cts. / (s s.p)]')
plt.tight_layout()
plt.legend()
plt.savefig(f'flux_energy', dpi=256)
