import matplotlib
import openmc

###############################################################################
#generate geometry plot of are (all safety rods fully inserted)
###############################################################################

h5m_filepath = 'h5m_files/rod_worth/ARE_pos_0..h5m'

#fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
salt = openmc.Material(name='salt', temperature = operating_temp)
salt.set_density('g/cm3',3.3142201)
salt.add_element('F',0.5309*1/2+0.4073*4/5+0.0618*4/5)
salt.add_element('Na',0.5309*1/2+0.4073*0/5+0.0618*0/5)
salt.add_element('Zr',0.5309*0/2+0.4073*1/5+0.0618*0/5)
salt.add_nuclide('U235',0.5309*0/2+0.4073*0/5+0.0618*0.9340*1/5)
salt.add_nuclide('U238',0.5309*0/2+0.4073*0/5+0.0618*0.066*1/5)

#moderator blocks
BeO = openmc.Material(name='BeO',temperature=977.5944)
BeO.add_element('Be',1.0)
BeO.add_element('O',1.0)
BeO.set_density('g/cm3',2.75)

#inconel
inconel = openmc.Material(name='inconel',temperature=977.5944)
inconel.add_element('Ni',78.5,percent_type='wo')
inconel.add_element('Cr',14.0,percent_type='wo')
inconel.add_element('Fe',6.5,percent_type='wo')
inconel.add_element('Mn',0.25,percent_type='wo')
inconel.add_element('Si',0.25,percent_type='wo')
inconel.add_element('Cu',0.2,percent_type='wo')
inconel.add_element('Co',0.2,percent_type='wo')
inconel.add_element('Al',0.2,percent_type='wo')
inconel.add_element('Ti',0.2,percent_type='wo')
inconel.add_element('Ta',0.5,percent_type='wo')
inconel.add_element('W',0.5,percent_type='wo')
inconel.add_element('Zn',0.2,percent_type='wo')
inconel.add_element('Zr',0.1,percent_type='wo')
inconel.add_element('C',0.08,percent_type='wo')
inconel.set_density('g/cm3',8.5)

#metal
metal = openmc.Material(name='metal',temperature=977.5944)
metal.add_element('Ni',78.5,percent_type='wo')
metal.add_element('Cr',14.0,percent_type='wo')
metal.add_element('Fe',6.5,percent_type='wo')
metal.add_element('Mn',0.25,percent_type='wo')
metal.add_element('Si',0.25,percent_type='wo')
metal.add_element('Cu',0.2,percent_type='wo')
metal.add_element('Co',0.2,percent_type='wo')
metal.add_element('Al',0.2,percent_type='wo')
metal.add_element('Ti',0.2,percent_type='wo')
metal.add_element('Ta',0.5,percent_type='wo')
metal.add_element('W',0.5,percent_type='wo')
metal.add_element('Zn',0.2,percent_type='wo')
metal.add_element('Zr',0.1,percent_type='wo')
metal.add_element('C',0.08,percent_type='wo')
metal.set_density('g/cm3',8.5)

#insulation
insulation = openmc.Material(name='insulation')
insulation.add_element('Si',1)
insulation.add_element('O',13)
insulation.add_element('Al',2)
insulation.add_element('Ca',1)
insulation.add_element('Fe',2)
insulation.add_element('K',2)
insulation.add_element('Na',2)
insulation.add_element('Ti',1)
insulation.set_density('g/cm3',2.24)

#coolant
coolant = openmc.Material(name='coolant')
coolant.add_element('Na',1.0)
coolant.set_density('g/cm3',0.78)

#helium
helium = openmc.Material(name='helium')
helium.add_element('He',1.0)
helium.set_density('g/cm3',1.03*(10**-4))

#stainless
stainless = openmc.Material(name='stainless',temperature=977.5944)
stainless.add_element('C',0.030,percent_type='wo')
stainless.add_element('Mn',2.00,percent_type='wo')
stainless.add_element('P',0.045,percent_type='wo')
stainless.add_element('S',0.030,percent_type='wo')
stainless.add_element('Si',0.75,percent_type='wo')
stainless.add_element('Cr',18.00,percent_type='wo')
stainless.add_element('Ni',8.0,percent_type='wo')
stainless.add_element('N',0.1,percent_type='wo')
stainless.set_density('g/cm3',8.5)

#absorber
boron = openmc.Material(name='boron')
boron.add_element('B',4.0)
boron.add_element('C',1.0)
boron.set_density('g/cm3',2.52)

#blanket
blanket = openmc.Material(name = 'blanket')
blanket.add_element('F',5.0)
blanket.add_element('Li',1.0)
blanket.add_element('Th',1.0)
blanket.set_density('g/cm3',5.0)

#shield
shield = openmc.Material(name = 'iron')
shield.add_element('Fe',1.0)
shield.set_density('g/cm3',7.874)

#filter
filter = openmc.Material(name = 'air')
filter.add_element('N',0.7803)
filter.add_element('O',0.21)
filter.add_element('Ar',0.93)
filter.add_element('C',0.04*1./3)
filter.add_element('O',0.04*2./3)
filter.set_density('g/cm3',0.001225)


mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,metal,stainless,boron,blanket,shield,filter])
mats.export_to_xml()

dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

#plotting geometry
plots = openmc.Plots()

x_width = 350
y_width = 350

#xy plot
#p1 = openmc.Plot()
#p1.width = (x_width,y_width)
#p1.pixels = (2000, 2000)
#p1.color_by = 'material'

#xz plot
p2 = openmc.Plot()
p2.basis = 'xz'
p2.width = (x_width,y_width)
p2.pixels = (1000, 1000)
p2.color_by = 'material'

p3 = openmc.Plot()
p3.basis = 'yz'
p3.width = (x_width,y_width)
p3.pixels = (1000, 1000)
p3.color_by = 'material'

#plots.append(p1)
plots.append(p2)
plots.append(p3)
plots.export_to_xml()

openmc.plot_geometry()
