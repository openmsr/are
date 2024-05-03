import openmc
import matplotlib.pyplot as plt
import numpy as np

from build_model import ARE_reactor

###############################################################################
#create .png files of photon flux (all safety rods inserted)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m')
ARE.bld_model()

#tallies
tallies = openmc.Tallies()

# particle filters
neutron_particle_filter=openmc.ParticleFilter(['neutron'])
photon_particle_filter=openmc.ParticleFilter(['photon'])

# energy binned filters
energy_bins = openmc.mgxs.GROUP_STRUCTURES['VITAMIN-J-175']
energy_filter = openmc.EnergyFilter(energy_bins)

#domain filters
print([m.id for m in ARE.materials if m.name=='salt'])
fuel_domain = openmc.MaterialFilter([m.id for m in ARE.materials if m.name=='salt'])
coolant_domain = openmc.MaterialFilter([m.id for m in ARE.materials if m.name=='coolant'])

# tallies
tallyEn0 = openmc.Tally(name='energy_n')
tallyEn0.filters = [energy_filter,neutron_particle_filter]
tallyEn0.scores = ['flux']
tallies.append(tallyEn0)

tallyEp0 = openmc.Tally(name='energy_p')
tallyEp0.filters = [energy_filter,photon_particle_filter]
tallyEp0.scores = ['flux']
tallies.append(tallyEp0)

tallyEn1 = openmc.Tally(name='energy_fuel_n')
tallyEn1.filters = [energy_filter,neutron_particle_filter,fuel_domain]
tallyEn1.scores = ['flux']
tallies.append(tallyEn1)

tallyEp1 = openmc.Tally(name='energy_fuel_p')
tallyEp1.filters = [energy_filter,photon_particle_filter,fuel_domain]
tallyEp1.scores = ['flux']
tallies.append(tallyEp1)

tallyEn1 = openmc.Tally(name='energy_coolant_n')
tallyEn1.filters = [energy_filter,neutron_particle_filter,coolant_domain]
tallyEn1.scores = ['flux']
tallies.append(tallyEn1)

tallyEp1 = openmc.Tally(name='energy_coolant_p')
tallyEp1.filters = [energy_filter,photon_particle_filter,coolant_domain]
tallyEp1.scores = ['flux']
tallies.append(tallyEp1)

# override the default set of tallies
ARE.model.tallies=tallies
ARE.model.settings.photon_transport=True

sp_filename = ARE.model.run()
sp = openmc.StatePoint(sp_filename)

n_tally0 = sp.get_tally(name='energy_n')
p_tally0 = sp.get_tally(name='energy_p')
n_tallyf = sp.get_tally(name='energy_fuel_n')
p_tallyf = sp.get_tally(name='energy_fuel_p')
n_tallyc = sp.get_tally(name='energy_coolant_n')
p_tallyc = sp.get_tally(name='energy_coolant_p')


fluxn0 = n_tally0.get_slice(scores=['flux'])
fluxp0 = p_tally0.get_slice(scores=['flux'])
fluxnf = n_tallyf.get_slice(scores=['flux'])
fluxpf = p_tallyf.get_slice(scores=['flux'])
fluxnc = n_tallyc.get_slice(scores=['flux'])
fluxpc = p_tallyc.get_slice(scores=['flux'])

energy_midpts=(energy_bins[:-1]+energy_bins[1:])*0.5

fig,ax = plt.subplots()
pos=ax.errorbar(energy_midpts,fluxn0.mean.squeeze(), yerr=fluxn0.std_dev.squeeze(), capsize=3, capthick=1, label='neutron flux')
pos=ax.errorbar(energy_midpts,fluxp0.mean.squeeze(), yerr=fluxp0.std_dev.squeeze(), capsize=3, capthick=1, label='photon flux')
ax.grid()
ax.set_title('flux overall')
ax.set_xscale('log')
ax.set_xlabel('energy [eV]')
ax.set_ylabel('flux [cts. / (s s.p)]')
plt.tight_layout()
plt.legend()
plt.savefig(f'flux_energy', dpi=256)

fig,ax = plt.subplots()
pos=ax.errorbar(energy_midpts,fluxnf.mean.squeeze(), yerr=fluxnf.std_dev.squeeze(), capsize=3, capthick=1, label='neutron flux')
pos=ax.errorbar(energy_midpts,fluxpf.mean.squeeze(), yerr=fluxpf.std_dev.squeeze(), capsize=3, capthick=1, label='photon flux')
ax.grid()
ax.set_title('flux in fuel salt')
ax.set_xscale('log')
ax.set_xlabel('energy [eV]')
ax.set_ylabel('flux [cts. / (s s.p)]')
plt.tight_layout()
plt.legend()
plt.savefig(f'flux_energy_fuel', dpi=256)

fig,ax = plt.subplots()
pos=ax.errorbar(energy_midpts,fluxnc.mean.squeeze(), yerr=fluxnc.std_dev.squeeze(), capsize=3, capthick=1, label='neutron flux')
pos=ax.errorbar(energy_midpts,fluxpc.mean.squeeze(), yerr=fluxpc.std_dev.squeeze(), capsize=3, capthick=1, label='photon flux')
ax.grid()
ax.set_title('flux in fuel salt')
ax.set_xscale('log')
ax.set_xlabel('energy [eV]')
ax.set_ylabel('flux [cts. / (s s.p)]')
plt.tight_layout()
plt.legend()
plt.savefig(f'flux_energy_coolant', dpi=256)
