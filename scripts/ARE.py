import matplotlib.pyplot as plt
from materials import *
import sys
import openmc

###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/ARE.h5m'

mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()


openmc.run()
