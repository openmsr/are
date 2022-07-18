import matplotlib.pyplot as plt
from materials import *
import sys
import openmc

###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted)
###############################################################################

h5m_filepath = 'h5m_files/ARE_2.h5m'

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
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
settings.max_lost_particles = 10000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#dag_univ = openmc.DAGMCUniverse(h5m_filepath)
#geom = openmc.Geometry(root=dag_univ)
#geom.export_to_xml()


openmc.run()
