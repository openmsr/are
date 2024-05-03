#!/usr/bin/env python

from build_model import ARE_reactor
###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted,
#  fuel salt at nominal composition)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m')
ARE.bld_model()
ARE.model.run()
