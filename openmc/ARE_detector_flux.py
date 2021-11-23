import matplotlib
import openmc
import h5py
import openmc.lib
import neutronics_material_maker as nmm

###############################################################################
#create .png file of photon flux (all safety rods inserted)
###############################################################################
# remove all old results file from the folder
try:
    get_ipython().system('rm *.xml *.ppm *.h5 *.out')
except :
    pass

assert(openmc.lib._dagmc_enabled())

#equilibrium operating temperature in kelvin
operating_temp = 977.59
path="/home/lorenzo/Documents/openmc_projects/are-main/openmc"
#Geometry
h5m_filepath = path+'/h5m_files/ARE_detector_body.h5m'
h5m_mesh_filepath = path+'/h5m_files/detector_body_mesh.h5m'

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

#detector
detector = openmc.Material(name = 'detector')
detector.add_element('H',2.0)
detector.add_element('O',1.0)
detector.set_density('g/cm3',1.0)

mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield,detector])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 150
settings.inactive = 20
settings.particles = 100000
settings.photon_transport = True
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#set a detector sphere
#sphere = openmc.Sphere(x0=250,r=50)
#inside_sphere = -sphere
#outside_sphere = +sphere
#cell = openmc.Cell()
#cell.region = sphere
#cell.fill = detector

# sets up mesh filters
dag_univ = openmc.DAGMCUniverse(h5m_filepath)
#dag_univ.add_cell(cell)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()
#plotting geometry
plots = openmc.Plots()
x_width = 600
y_width = 600
#xz plot
p1 = openmc.Plot()
p1.basis = 'xz'
p1.width = (x_width,y_width)
p1.pixels = (1000, 1000)
p1.color_by = 'material'
plots.append(p1)
plots.export_to_xml()
openmc.plot_geometry()
#sets UnstructuredMesh for tallies
mesh = openmc.UnstructuredMesh(h5m_mesh_filepath,library="moab")
mesh_filter = openmc.MeshFilter(mesh)

# sets up filters for the tallies
PhotonParticleFilter = openmc.ParticleFilter(['photon'])
NeutronParticleFilter = openmc.ParticleFilter(['neutron'])
tally_p = openmc.Tally(name="photon_flux_cell")
tally_n = openmc.Tally(name="neutron_flux_cell")
tally_p.scores = ['flux']
tally_n.scores = ['flux']
tally_p.filters = [mesh_filter,PhotonParticleFilter]
tally_n.filters = [mesh_filter,NeutronParticleFilter]
tally_hr.scores = ['heating']
#Append tallies
tallies = openmc.Tallies()
tallies.append(tally_p)
tallies.append(tally_n)
tallies.append(tally_hr)
tallies.export_to_xml()
# combine all the required parts to make a model
openmc.run()
