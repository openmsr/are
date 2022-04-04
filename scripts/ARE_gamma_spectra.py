import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
# Generates photon spectra for each material in the ARE

# Assumes 0.5m neutron blanket and 0.5m iron shield.
# Run geometry_plotter on 'h5m_files/ARE_gamma.h5m' to visualize

# filter cell is a 1mm cylinder around the iron shield, defined here as air
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59

#Geometry
h5m_filepath = 'h5m_files/ARE_gamma.h5m'

#materials
mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield,filter])
mats.export_to_xml()

#settings
settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.photon_transport = True
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#cad geometry
dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

#tallies
#creates an empty tally object
tallies = openmc.Tallies()

# sets up filters for the tallies
photon_particle_filter = openmc.ParticleFilter(['photon'])  # note the use of photons here
energy_bins = openmc.mgxs.GROUP_STRUCTURES['VITAMIN-J-175']
energy_filter = openmc.EnergyFilter(energy_bins)

# salt
cell_spectra_tally_1 = openmc.Tally(name='salt_spectrum')
cell_spectra_tally_1.scores = ['flux']
cell_spectra_tally_1.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(4)]

# moderator
cell_spectra_tally_2 = openmc.Tally(name='moderator_spectrum')
cell_spectra_tally_2.scores = ['flux']
cell_spectra_tally_2.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(5)]

# inconel
cell_spectra_tally_3 = openmc.Tally(name='inconel_spectrum')
cell_spectra_tally_3.scores = ['flux']
cell_spectra_tally_3.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(6)]

# insulation
#cell_spectra_tally_4 = openmc.Tally(name='cell_spectra_tally_4')
#cell_spectra_tally_4.scores = ['flux']
#cell_spectra_tally_4.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(8)]

# coolant
cell_spectra_tally_5 = openmc.Tally(name='coolant_spectrum')
cell_spectra_tally_5.scores = ['flux']
cell_spectra_tally_5.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(9)]

# helium
cell_spectra_tally_6 = openmc.Tally(name='helium_spectrum')
cell_spectra_tally_6.scores = ['flux']
cell_spectra_tally_6.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(10)]

# stainless
cell_spectra_tally_7 = openmc.Tally(name='stainless_spectrum')
cell_spectra_tally_7.scores = ['flux']
cell_spectra_tally_7.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(11)]

# boron
cell_spectra_tally_8 = openmc.Tally(name='boron_spectrum')
cell_spectra_tally_8.scores = ['flux']
cell_spectra_tally_8.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(12)]

# blanket
cell_spectra_tally_9 = openmc.Tally(name='blanket_spectrum')
cell_spectra_tally_9.scores = ['flux']
cell_spectra_tally_9.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(13)]

# shield
cell_spectra_tally_10 = openmc.Tally(name='shield_spectrum')
cell_spectra_tally_10.scores = ['flux']
cell_spectra_tally_10.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(14)]

# air
cell_spectra_tally_11 = openmc.Tally(name='filter_spectrum')
cell_spectra_tally_11.scores = ['flux']
cell_spectra_tally_11.filters = [photon_particle_filter, energy_filter,openmc.CellFilter(15)]

#comment out any of the below to modify which tallies end up in the statepoint
tallies.append(cell_spectra_tally_1)
tallies.append(cell_spectra_tally_2)
tallies.append(cell_spectra_tally_3)
#tallies.append(cell_spectra_tally_4)
tallies.append(cell_spectra_tally_5)
tallies.append(cell_spectra_tally_6)
tallies.append(cell_spectra_tally_7)
tallies.append(cell_spectra_tally_8)
tallies.append(cell_spectra_tally_9)
tallies.append(cell_spectra_tally_10)
tallies.append(cell_spectra_tally_11)

# combine all the required parts to make a model
model = openmc.model.Model(geom, mats, settings, tallies)

model.run()
