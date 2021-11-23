import matplotlib.pyplot as plt
import openmc

###############################################################################
# Generates photon spectra for each material in the ARE

# Assumes 0.5m neutron blanket and 0.5m iron shield.
# Run geometry_plotter on 'h5m_files/ARE_gamma_3.h5m' to visualize

# filter cell is a 1mm cylinder around the iron shield, defined here as air
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59

#Geometry
h5m_filepath = 'h5m_files/ARE_gamma_3.h5m'

#fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
salt = openmc.Material(name='salt', temperature = operating_temp)
salt.set_density('g/cm3',3.3142201)
salt.add_element('F',0.5309*1/2+0.4073*4/5+0.0618*4/5)
salt.add_element('Na',0.5309*1/2+0.4073*0/5+0.0618*0/5)
salt.add_element('Zr',0.5309*0/2+0.4073*1/5+0.0618*0/5)
salt.add_nuclide('U235',0.5309*0/2+0.4073*0/5+0.0618*0.9340*1/5)
salt.add_nuclide('U238',0.5309*0/2+0.4073*0/5+0.0618*0.066*1/5)

#moderator blocks
BeO = openmc.Material(name='BeO',temperature = operating_temp)
BeO.add_element('Be',1.0)
BeO.add_element('O',1.0)
BeO.set_density('g/cm3',2.75)

#inconel
trace = 0.01
inconel = openmc.Material(name='inconel',temperature = operating_temp)
inconel.add_element('Ni',78.5,percent_type='wo')
inconel.add_element('Cr',14.0,percent_type='wo')
inconel.add_element('Fe',6.5,percent_type='wo')
inconel.add_element('Mn',0.25,percent_type='wo')
inconel.add_element('Si',0.25,percent_type='wo')
inconel.add_element('Cu',0.2,percent_type='wo')
inconel.add_element('Co',0.2,percent_type='wo')
inconel.add_element('Al',0.2,percent_type='wo')
inconel.add_element('Ti',0.2,percent_type='wo')
inconel.add_element('Ta',0.5,percent_type='wo')
inconel.add_element('W',0.5,percent_type='wo')
inconel.add_element('Zn',0.2,percent_type='wo')
inconel.add_element('Zr',0.1,percent_type='wo')
inconel.add_element('C',trace,percent_type='wo')
inconel.add_element('Mo',trace,percent_type='wo')
inconel.add_element('Ag',trace,percent_type='wo')
inconel.add_element('B',trace,percent_type='wo')
inconel.add_element('Ba',trace,percent_type='wo')
inconel.add_element('Be',trace,percent_type='wo')
inconel.add_element('Ca',trace,percent_type='wo')
inconel.add_element('Cd',trace,percent_type='wo')
inconel.add_element('V',trace,percent_type='wo')
inconel.add_element('Sn',trace,percent_type='wo')
inconel.add_element('Mg',trace,percent_type='wo')
inconel.set_density('g/cm3',8.5)

#insulation
insulation = openmc.Material(name='insulation')
insulation.add_element('Si',1)
insulation.add_element('O',13)
insulation.add_element('Al',2)
insulation.add_element('Ca',1)
insulation.add_element('Fe',2)
insulation.add_element('K',2)
insulation.add_element('Na',2)
insulation.add_element('Ti',1)
insulation.set_density('g/cm3',2.24)

#coolant
coolant = openmc.Material(name='coolant',temperature = operating_temp)
coolant.add_element('Na',1.0)
coolant.set_density('g/cm3',0.78)

#helium
helium = openmc.Material(name='helium')
helium.add_element('He',1.0)
helium.set_density('g/cm3',1.03*(10**-4))

#stainless
stainless = openmc.Material(name='stainless')
stainless.add_element('C',0.030,percent_type='wo')
stainless.add_element('Mn',2.00,percent_type='wo')
stainless.add_element('P',0.045,percent_type='wo')
stainless.add_element('S',0.030,percent_type='wo')
stainless.add_element('Si',0.75,percent_type='wo')
stainless.add_element('Cr',18.00,percent_type='wo')
stainless.add_element('Ni',8.0,percent_type='wo')
stainless.add_element('N',0.1,percent_type='wo')
stainless.set_density('g/cm3',8.5)

#absorber
boron = openmc.Material(name = 'boron')
boron.add_element('B',4.0)
boron.add_element('C',1.0)
boron.set_density('g/cm3',2.52)

#blanket LiF-ThF4 78-22
blanket = openmc.Material(name = 'blanket')
blanket.add_element('F',0.78*1/2+0.22*4/5)
blanket.add_element('Li',0.78*1/2)
blanket.add_element('Th',0.22*1/5)
blanket.set_density('g/cm3',6.00)

#shield
shield = openmc.Material(name = 'iron')
shield.add_element('Fe',1.0)
shield.set_density('g/cm3',7.86)

#filter
filter = openmc.Material(name = 'air')
filter.add_element('N',0.7803)
filter.add_element('O',0.21)
filter.add_element('Ar',0.93)
filter.add_element('C',0.04*1./3)
filter.add_element('O',0.04*2./3)
filter.set_density('g/cm3',0.001225)

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
tallies.append(cell_spectra_tally_4)
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
