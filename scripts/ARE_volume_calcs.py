import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#stochastic volume calculation for ARE parts
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59

#Geometry
h5m_filepath = 'h5m_files/ARE.h5m'

mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield,filter])
mats.export_to_xml()

#geometry
graveyard=openmc.Sphere(r=10000,boundary_type='vacuum')

cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True,universe_id=996 )

cad_cell = openmc.Cell(cell_id=997 , region= -graveyard, fill= cad_univ)

root = openmc.Universe(universe_id=998)
root.add_cells([cad_cell])
geometry = openmc.Geometry(root)
geometry.export_to_xml()

#volume calculation
ll = [-350,-350,-350]
ur = [350,350,350]
mag = 6
vol_calc_salt = openmc.VolumeCalculation([salt],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_moderator = openmc.VolumeCalculation([BeO],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_inconel = openmc.VolumeCalculation([inconel],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_insulation = openmc.VolumeCalculation([insulation],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_coolant = openmc.VolumeCalculation([coolant],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_helium = openmc.VolumeCalculation([helium],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_stainless = openmc.VolumeCalculation([stainless],int(10**mag),lower_left=ll,upper_right=ur)
vol_calc_boron = openmc.VolumeCalculation([boron],int(10**mag),lower_left=ll,upper_right=ur)

#settings
settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.volume_calculations = [vol_calc_salt,
                                vol_calc_moderator,
                                vol_calc_inconel,
                                vol_calc_insulation,
                                vol_calc_coolant,
                                vol_calc_helium,
                                vol_calc_stainless,
                                vol_calc_boron]
settings.run_mode = 'volume'
settings.export_to_xml()

openmc.calculate_volumes()
