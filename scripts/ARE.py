import matplotlib.pyplot as plt
from materials import *
import openmc

###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted)
###############################################################################

h5m_filepath = 'h5m_files/ARE.h5m'

#geometry
graveyard=openmc.Sphere(r=10000,boundary_type='vacuum')

cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True,universe_id=996 )

cad_cell = openmc.Cell(cell_id=997 , region= -graveyard, fill= cad_univ)

root = openmc.Universe(universe_id=998)
root.add_cells([cad_cell])
geometry = openmc.Geometry(root)
geometry.export_to_xml()

mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 10
settings.inactive = 1
settings.particles = 100
settings.max_lost_particles = 1000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.track=[[10,1,55]]
settings.cross_sections='/home/luke/openmc/nuclear_data/endfb71_hdf5/cross_sections.xml'
settings.export_to_xml()

#dag_univ = openmc.DAGMCUniverse(h5m_filepath)
#geom = openmc.Geometry(root=dag_univ)
#geom.export_to_xml()


openmc.run()
