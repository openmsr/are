import matplotlib
import openmc
import h5py
import openmc.lib
import neutronics_material_maker as nmm
from materials import *

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

# materials
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
