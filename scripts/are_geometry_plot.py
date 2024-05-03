from build_model import ARE_reactor
from initialize_materials import *
import subprocess as sp
###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted,
#  fuel salt at nominal composition)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m')
ARE.bld_model()
#plotting geometry
plots = openmc.Plots()

x_width = 300
y_width = 300

#xy plot
p1 = openmc.Plot()
p1.width = (x_width,y_width)
p1.pixels = (2048, 2048)
p1.color_by = 'material'
p1.filename='are_xy'

#xz plot (split plane)
p2 = openmc.Plot()
p2.basis = 'xz'
p2.origin = (0,0,0)
p2.width = (x_width,y_width)
p2.pixels = (2048, 2048)
p2.color_by = 'material'
p2.filename='are_xz'

p3 = openmc.Plot()
p3.basis = 'yz'
p3.width = (x_width,y_width)
p3.origin = (0,0,0)
p3.pixels = (2048, 2048)
p3.color_by = 'material'
p3.filename='are_yz'

plots.append(p1)
plots.append(p2)
plots.append(p3)

ARE.plots=plots
ARE.plots.export_to_xml()
sp.run(['openmc','-p'])
