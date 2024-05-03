#!/usr/bin/env python
import openmc
from build_model import ARE_reactor
###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted,
#  fuel salt at nominal composition)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m')
ARE.bld_model()
ARE.model.settings.run_mode='volume'
bb = ARE.model.geometry.bounding_box
print(bb)
vol_calc=openmc.VolumeCalculation(ARE.materials,1000000,lower_left=bb[0],upper_right=bb[1])
ARE.model.settings.volume_calculations=vol_calc

ARE.model.run()
