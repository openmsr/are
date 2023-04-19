import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#create .png file of neutron flux (all safety rods inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/ARE_pos_0..h5m'
graveyard=openmc.Sphere(r=10000,boundary_type='vacuum')
cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True,universe_id=996 )
cad_cell = openmc.Cell(cell_id=997 , region= -graveyard, fill= cad_univ)
root = openmc.Universe(universe_id=998)
root.add_cells([cad_cell])
geometry = openmc.Geometry(root)
geometry.export_to_xml()

#materials
mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield])
mats.export_to_xml()

#settings
settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 50
settings.inactive = 20
settings.particles = 30000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#tallies
tallies = openmc.Tallies()

# resolution
res = 200

mesh = openmc.RegularMesh()
mesh.dimension = [res,res,res]
mesh.lower_left = [-70,-70,0]
mesh.upper_right = [70,70,120]

mesh_filter = openmc.MeshFilter(mesh)

tally = openmc.Tally(name='flux')
tally.filters = [mesh_filter]
tally.scores = ['flux','fission']
tallies.append(tally)

tallies.export_to_xml()

model = openmc.model.Model(geometry, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)

s_tally = sp.get_tally(scores=['flux','fission'])
flux = s_tally.get_slice(scores=['flux'])
fission = s_tally.get_slice(scores=['fission'])

flux.std_dev.shape = (res,res,res)
flux.mean.shape = (res,res,res)
fission.std_dev.shape = (res,res,res)
fission.mean.shape = (res,res,res)


split_index = int(res/2)

# flux
# xy plot
xy_mean = flux.mean[split_index,:,:]
fig,ax = plt.subplots()
pos = ax.imshow(xy_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('mean neutron flux: xy plane')
plt.colorbar(pos,ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_xy')

# xz plot
xz_mean = flux.mean[:,split_index, :]
fig,ax = plt.subplots()
pos = ax.imshow(xz_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Z / cm')
ax.set_title('mean neutron flux: xz plane')
plt.colorbar(pos,ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_xz')

# yz plot
yz_mean = flux.mean[:,:,split_index]
fig,ax = plt.subplots()
pos = ax.imshow(yz_mean)
ax.set_xlabel('Y / cm')
ax.set_ylabel('Z / cm')
ax.set_title('mean neutron flux: yz plane')
plt.colorbar(pos, ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_yz')

# fission 
# xy plot
xy_mean = fission.mean[split_index,:,:]
fig,ax = plt.subplots()
pos = ax.imshow(xy_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('fission events: xy plane')
plt.colorbar(pos,ax=ax,label=r'Fission [reactions/cm$^2$-s]')
plt.savefig('fission_xy')

# xz plot
xz_mean = fission.mean[:,split_index, :]
fig,ax = plt.subplots()
pos = ax.imshow(xz_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Z / cm')
ax.set_title('fission events: xz plane')
plt.colorbar(pos,ax=ax,label=r'Fission [reactions/cm$^2$-s]')
plt.savefig('fission_xz')

# yz plot
yz_mean = fission.mean[:,:,split_index]
fig,ax = plt.subplots()
pos = ax.imshow(yz_mean)
ax.set_xlabel('Y / cm')
ax.set_ylabel('Z / cm')
ax.set_title('fission events: yz plane')
plt.colorbar(pos, ax=ax,label=r'Fission [reactions/cm$^2$-s]')
plt.savefig('fission_yz')