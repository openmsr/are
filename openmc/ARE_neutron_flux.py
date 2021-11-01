import matplotlib.pyplot as plt
import openmc

###############################################################################
#create .png file of neutron flux (all safety rods inserted)
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59

#Geometry
h5m_filepath = 'h5m_files/rod_worth/ARE_pos_0..h5m'

#fuel salt
NaF = openmc.Material(name='NaF',temperature = operating_temp)
NaF.add_element('Na',1.0)
NaF.add_element('F',1.0)
#NaF.set_density('g/cm3',2.56)

ZrF = openmc.Material(name='ZrF',temperature = operating_temp)
ZrF.add_element('Zr',1.0)
ZrF.add_element('F',4.0)
#ZrF.set_density('g/cm3',4.43)

UF = openmc.Material(name='UF',temperature = operating_temp)
UF.add_nuclide('U235',.9340)
UF.add_nuclide('U238',.066)
UF.add_element('F',4.0)
#UF.set_density('g/cm3',6.7)

salt = openmc.Material.mix_materials([NaF,ZrF,UF],[.2034,.6212,.1754],'wo',name='salt')
salt.set_density('g/cm3',3.3142201)
salt.temperature = operating_temp

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


mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 5000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

tallies = openmc.Tallies()

mesh = openmc.RegularMesh()
mesh.dimension = [1000,1000]
mesh.lower_left = [-300,-300]
mesh.upper_right = [300,300]

mesh_filter = openmc.MeshFilter(mesh)

tally = openmc.Tally(name='flux')
tally.filters = [mesh_filter]
tally.scores = ['flux','fission']
tallies.append(tally)

tallies.export_to_xml()

model = openmc.model.Model(geom, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)
s_tally = sp.get_tally(scores=['flux','fission'])

flux = s_tally.get_slice(scores=['flux'])
fission = s_tally.get_slice(scores=['fission'])

flux.std_dev.shape = (1000,1000)
flux.mean.shape = (1000,1000)
fission.std_dev.shape = (1000,1000)
fission.mean.shape = (1000,1000)

fig = plt.subplot(121)
fig.axis([350,650,350,650])
fig.pixels = (2000,2000)
fig.imshow(flux.mean)
plt.savefig('neutron_flux', dpi=2000)
