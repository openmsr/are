import sys
sys.path.append('/opt/openmc/')
import openmc

###############################################################################
# set of different fuel salts for the aircraft reactor experiment
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 977.59


#ARE material definitions

h = 0.03

# run 1
salt1 = openmc.Material(name='salt', temperature = operating_temp)
salt1.set_density('g/cm3',3.3142201)
salt1.add_element('Na',10.99,percent_type='wo')
salt1.add_element('Zr',43.60,percent_type='wo')
salt1.add_element('F',45.41,percent_type='wo')
salt1.add_nuclide('U235',0.00,percent_type='wo')

# run 2
salt2 = openmc.Material(name='salt', temperature = operating_temp)
salt2.set_density('g/cm3',3.3142201)
salt2.add_element('Na',10.41,percent_type='wo')
salt2.add_element('Zr',43.02,percent_type='wo')
salt2.add_element('F',44.83,percent_type='wo')
salt2.add_nuclide('U235',01.74,percent_type='wo')

# run 3
salt3 = openmc.Material(name='salt', temperature = operating_temp)
salt3.set_density('g/cm3',3.3142201)
salt3.add_element('Na',9.94,percent_type='wo')
salt3.add_element('Zr',42.56,percent_type='wo')
salt3.add_element('F',44.36,percent_type='wo')
salt3.add_nuclide('U235',3.14,percent_type='wo')

# run 4
salt4 = openmc.Material(name='salt', temperature = operating_temp)
salt4.set_density('g/cm3',3.3142201)
salt4.add_element('Na',9.41,percent_type='wo')
salt4.add_element('Zr',42.03,percent_type='wo')
salt4.add_element('F',43.83,percent_type='wo')
salt4.add_nuclide('U235',4.72,percent_type='wo')

# run 5
salt5 = openmc.Material(name='salt', temperature = operating_temp)
salt5.set_density('g/cm3',3.3142201)
salt5.add_element('Na',8.92,percent_type='wo')
salt5.add_element('Zr',41.53,percent_type='wo')
salt5.add_element('F',43.33,percent_type='wo')
salt5.add_nuclide('U235',6.22,percent_type='wo')

# run 6
salt6 = openmc.Material(name='salt', temperature = operating_temp)
salt6.set_density('g/cm3',3.3142201)
salt6.add_element('Na',8.45,percent_type='wo')
salt6.add_element('Zr',41.07,percent_type='wo')
salt6.add_element('F',42.87,percent_type='wo')
salt6.add_nuclide('U235',7.61,percent_type='wo')

# run 7
salt7 = openmc.Material(name='salt', temperature = operating_temp)
salt7.set_density('g/cm3',3.3142201)
salt7.add_element('Na',8.03,percent_type='wo')
salt7.add_element('Zr',40.64,percent_type='wo')
salt7.add_element('F',42.44,percent_type='wo')
salt7.add_nuclide('U235',8.89,percent_type='wo')

# run 8
salt8 = openmc.Material(name='salt', temperature = operating_temp)
salt8.set_density('g/cm3',3.3142201)
salt8.add_element('Na',7.77,percent_type='wo')
salt8.add_element('Zr',40.39,percent_type='wo')
salt8.add_element('F',42.19,percent_type='wo')
salt8.add_nuclide('U235',9.605,percent_type='wo')

# run 9
salt9 = openmc.Material(name='salt', temperature = operating_temp)
salt9.set_density('g/cm3',3.3142201)
salt9.add_element('Na',7.64,percent_type='wo')
salt9.add_element('Zr',40.25,percent_type='wo')
salt9.add_element('F',42.05,percent_type='wo')
salt9.add_nuclide('U235',10.06,percent_type='wo')

# run 10
salt10 = openmc.Material(name='salt', temperature = operating_temp)
salt10.set_density('g/cm3',3.3142201)
salt10.add_element('Na',7.44,percent_type='wo')
salt10.add_element('Zr',40.06,percent_type='wo')
salt10.add_element('F',41.86,percent_type='wo')
salt10.add_nuclide('U235',10.64,percent_type='wo')

# run 11
salt11 = openmc.Material(name='salt', temperature = operating_temp)
salt11.set_density('g/cm3',3.3142201)
salt11.add_element('Na',7.26,percent_type='wo')
salt11.add_element('Zr',39.88,percent_type='wo')
salt11.add_element('F',41.68,percent_type='wo')
salt11.add_nuclide('U235',11.18,percent_type='wo')

# run 12 (critical)
salt12 = openmc.Material(name='salt', temperature = operating_temp)
salt12.set_density('g/cm3',3.3142201)
salt12.add_element('Na',7.13,percent_type='wo')
salt12.add_element('Zr',39.75,percent_type='wo')
salt12.add_element('F',41.55,percent_type='wo')
salt12.add_nuclide('U235',11.57,percent_type='wo')

# shim rod calibration fuels
salt_8A = openmc.Material(name='salt', temperature = operating_temp)
salt_8A.set_density('g/cm3',3.27578)
salt_8A.add_element('Na',11.10,percent_type='wo')
salt_8A.add_element('Zr',36.02,percent_type='wo')
salt_8A.add_element('F',42.53,percent_type='wo')
salt_8A.add_nuclide('U235',9.66,percent_type='wo')
salt_8A.add_nuclide('U238',0.69,percent_type='wo')

# shim rod calibration fuels
salt_9B = openmc.Material(name='salt', temperature = operating_temp)
salt_9B.set_density('g/cm3',3.28378)
salt_9B.add_element('Na',11.11,percent_type='wo')
salt_9B.add_element('Zr',35.70,percent_type='wo')
salt_9B.add_element('F',42.40,percent_type='wo')
salt_9B.add_nuclide('U235',10.07,percent_type='wo')
salt_9B.add_nuclide('U238',0.72,percent_type='wo')

# shim rod calibration fuels
salt_10C = openmc.Material(name='salt', temperature = operating_temp)
salt_10C.set_density('g/cm3',3.29500)
salt_10C.add_element('Na',11.12,percent_type='wo')
salt_10C.add_element('Zr',35.25,percent_type='wo')
salt_10C.add_element('F',42.23,percent_type='wo')
salt_10C.add_nuclide('U235',10.64,percent_type='wo')
salt_10C.add_nuclide('U238',0.76,percent_type='wo')

# shim rod calibration fuels
salt_11C = openmc.Material(name='salt', temperature = operating_temp)
salt_11C.set_density('g/cm3',3.30621)
salt_11C.add_element('Na',11.12,percent_type='wo')
salt_11C.add_element('Zr',34.82,percent_type='wo')
salt_11C.add_element('F',42.07,percent_type='wo')
salt_11C.add_nuclide('U235',11.18,percent_type='wo')
salt_11C.add_nuclide('U238',0.80,percent_type='wo')

# shim rod calibration fuels
salt_12B = openmc.Material(name='salt', temperature = operating_temp)
salt_12B.set_density('g/cm3',3.3142201)
salt_12B.add_element('Na',11.13,percent_type='wo')
salt_12B.add_element('Zr',35.70,percent_type='wo')
salt_12B.add_element('F',41.96,percent_type='wo')
salt_12B.add_nuclide('U235',11.57,percent_type='wo')
salt_12B.add_nuclide('U238',0.83,percent_type='wo')
