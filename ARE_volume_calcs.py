import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#stochastic volume calculation for ARE parts
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59

#Geometry
h5m_filepath = 'h5m_files/ARE_gamma_3.h5m'

mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield,filter])
mats.export_to_xml()

#cad geometry
dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

#volume calculation
lower_left = [-350,-350,-350]
upper_right = [350,350,350]
mag = 6
vol_calc_salt = openmc.VolumeCalculation([salt],int(10**mag))
vol_calc_moderator = openmc.VolumeCalculation([BeO],int(10**mag))
vol_calc_inconel = openmc.VolumeCalculation([inconel],int(10**mag))
vol_calc_insulation = openmc.VolumeCalculation([insulation],int(10**mag))
vol_calc_coolant = openmc.VolumeCalculation([coolant],int(10**mag))
vol_calc_helium = openmc.VolumeCalculation([helium],int(10**mag))
vol_calc_stainless = openmc.VolumeCalculation([stainless],int(10**mag))
vol_calc_boron = openmc.VolumeCalculation([boron],int(10**mag))

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
