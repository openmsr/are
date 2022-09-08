import sys
sys.path.append('/opt/openmc/')
import openmc


#equilibrium operating temperature in kelvin
operating_temp = 977.59


#ARE material definitions

#fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
salt = openmc.Material(name='salt', temperature = operating_temp)
salt.set_density('g/cm3',3.3142201)
salt.add_element('F',0.5309*1/2+0.4073*4/5+0.0618*4/5)
salt.add_element('Na',0.5309*1/2+0.4073*0/5+0.0618*0/5)
salt.add_element('Zr',0.5309*0/2+0.4073*1/5+0.0618*0/5)
salt.add_nuclide('U235',0.5309*0/2+0.4073*0/5+0.0618*0.9340*1/5)
salt.add_nuclide('U238',0.5309*0/2+0.4073*0/5+0.0618*0.066*1/5)

#moderator blocks
BeO = openmc.Material(name='BeO',temperature = operating_temp)
BeO.add_element('Be',1.0)
BeO.add_element('O',1.0)
BeO.set_density('g/cm3',2.75)

#inconel
trace = 0.01
inconel = openmc.Material(name='inconel',temperature = operating_temp)
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
inconel.add_element('C',trace,percent_type='wo')
inconel.add_element('Mo',trace,percent_type='wo')
inconel.add_element('Ag',trace,percent_type='wo')
inconel.add_element('B',trace,percent_type='wo')
inconel.add_element('Ba',trace,percent_type='wo')
inconel.add_element('Be',trace,percent_type='wo')
inconel.add_element('Ca',trace,percent_type='wo')
inconel.add_element('Cd',trace,percent_type='wo')
inconel.add_element('V',trace,percent_type='wo')
inconel.add_element('Sn',trace,percent_type='wo')
inconel.add_element('Mg',trace,percent_type='wo')
inconel.set_density('g/cm3',8.5)

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
coolant = openmc.Material(name='coolant',temperature = operating_temp)
coolant.add_element('Na',1.0)
coolant.set_density('g/cm3',0.78)

#helium
helium = openmc.Material(name='helium')
helium.add_element('He',1.0)
helium.set_density('g/cm3',1.03*(10**-4))

#stainless https://www.aesteiron.com/sa240-304l-stainless-steel-sheet-plate.html
stainless = openmc.Material(name='stainless')
stainless.add_element('C',0.030,percent_type='wo')
stainless.add_element('Mn',2.00,percent_type='wo')
stainless.add_element('P',0.045,percent_type='wo')
stainless.add_element('S',0.030,percent_type='wo')
stainless.add_element('Si',0.75,percent_type='wo')
stainless.add_element('Cr',18.00,percent_type='wo')
stainless.add_element('Ni',8.0,percent_type='wo')
stainless.add_element('N',0.1,percent_type='wo')
stainless.add_element('Fe',39.045,percent_type='wo')
stainless.set_density('g/cm3',8.5)

#absorber
boron = openmc.Material(name = 'boron')
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
