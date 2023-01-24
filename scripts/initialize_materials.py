import sys
sys.path.append('/opt/openmc/')
import openmc


def create_materials(operating_temp):
    #ARE material definitions

    #fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
    salt = openmc.Material(name='salt', temperature = operating_temp)
    salt.add_element('F',41.96,percent_type='wo')
    salt.add_element('Na',11.13,percent_type='wo')
    salt.add_element('Zr',34.52,percent_type='wo')
    salt.add_nuclide('U235',11.57,percent_type='wo')
    salt.add_nuclide('U238',11.57,percent_type='wo')
    salt.set_density('g/cm3',3.3142201)

    #moderator blocks
    BeO = openmc.Material(name='BeO',temperature = operating_temp)
    BeO.add_element('Be',35.8718,percent_type='wo')
    BeO.add_element('O',63.6819,percent_type='wo')

    # impurities (ORNL-1845 Appendix B)
    BeO.add_element('Si',0.2352,percent_type='wo')
    BeO.add_element('Al',0.0458,percent_type='wo')
    BeO.add_element('Pb',0.0744,percent_type='wo')
    BeO.add_element('Ni',0.0094,percent_type='wo')
    BeO.add_element('Mn',0.0022,percent_type='wo')
    BeO.add_element('Co',0.0002,percent_type='wo')
    BeO.add_element('Na',0.0605,percent_type='wo')
    BeO.add_element('Mg',0.0097,percent_type='wo')
    BeO.add_element('K',0.0078,percent_type='wo')
    BeO.add_element('Li',0.0003,percent_type='wo')
    BeO.add_element('Ag',0.0009,percent_type='wo')

    #BeO.add_element('Be',1.0)
    #BeO.add_element('O',1.0)
    BeO.set_density('g/cm3',2.75*0.968266752)

    #inconel
    inconel = openmc.Material(name='inconel',temperature = operating_temp)

    # test
    #inconel.add_element('Ni',52.50,percent_type='wo')
    #inconel.add_element('Cr',19.00,percent_type='wo')
    #inconel.add_element('Nb',5.125,percent_type='wo')
    #inconel.add_element('Mo',3.05,percent_type='wo')
    #nconel.add_element('Al',0.5,percent_type='wo')
    #inconel.add_element('Ti',0.9,percent_type='wo')
    #inconel.add_element('Mn',0.35,percent_type='wo')
    #inconel.add_element('Si',0.35,percent_type='wo')
    #inconel.add_element('B',0.006,percent_type='wo')
    #inconel.add_element('C',0.08,percent_type='wo')
    #inconel.add_element('S',0.15,percent_type='wo')
    #inconel.add_element('Fe',17.839,percent_type='wo')

    # from ORNL-2264 (average)
    inconel.add_element('Ni',76.5,percent_type='wo')
    inconel.add_element('Cr',15.275,percent_type='wo')
    inconel.add_element('Fe',7.375,percent_type='wo')
    inconel.add_element('Mn',0.2075,percent_type='wo')
    inconel.add_element('C',0.035,percent_type='wo')
    inconel.add_element('Cu',0.12,percent_type='wo')
    inconel.add_element('Si',0.175,percent_type='wo')
    inconel.add_element('S',0.007,percent_type='wo')
    inconel.add_element('Al',0.105,percent_type='wo')
    inconel.add_element('Ti',0.1725,percent_type='wo')
    inconel.add_element('B',0.04625,percent_type='wo')
    inconel.add_element('N',0.0295*2,percent_type='wo')

    # from ORNL-1845
    #trace = 0.0001
    #inconel.add_element('Ni',78.5,percent_type='wo')
    #inconel.add_element('Cr',14.0,percent_type='wo')
    #inconel.add_element('Fe',6.5,percent_type='wo')
    #inconel.add_element('Mn',0.25,percent_type='wo')
    #nconel.add_element('Si',0.25,percent_type='wo')
    #inconel.add_element('Cu',0.2,percent_type='wo')
    #nconel.add_element('Co',0.2,percent_type='wo')
    #inconel.add_element('Al',0.2,percent_type='wo')
    #inconel.add_element('Ti',0.2,percent_type='wo')
    #nconel.add_element('Ta',0.5,percent_type='wo')
    #inconel.add_element('W',0.5,percent_type='wo')
    #inconel.add_element('Si',0.25,percent_type='wo')
    #inconel.add_element('Cu',0.2,percent_type='wo')
    #inconel.add_element('Co',0.2,percent_type='wo')
    #inconel.add_element('Al',0.2,percent_type='wo')
    #nconel.add_element('Ti',0.2,percent_type='wo')
    #inconel.add_element('Ta',0.5,percent_type='wo')
    #nconel.add_element('W',0.5,percent_type='wo')
    #inconel.add_element('Zn',0.2,percent_type='wo')
    #inconel.add_element('Zr',0.1,percent_type='wo')
    #inconel.add_element('C',trace,percent_type='wo')
    #inconel.add_element('Mo',trace,percent_type='wo')
    #inconel.add_element('Ag',trace,percent_type='wo')
    #inconel.add_element('B',trace,percent_type='wo')
    #inconel.add_element('Ba',trace,percent_type='wo')
    #inconel.add_element('Be',trace,percent_type='wo')
    #inconel.add_element('Ca',trace,percent_type='wo')
    #inconel.add_element('Cd',trace,percent_type='wo')
    #inconel.add_element('V',trace,percent_type='wo')
    #inconel.add_element('Sn',trace,percent_type='wo')
    #inconel.add_element('Mg',trace,percent_type='wo')
    inconel.set_density('g/cm3',8.5)

    #insulation
    insulation = openmc.Material(name='insulation',temperature = operating_temp)
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
    helium = openmc.Material(name='helium',temperature = operating_temp)
    helium.add_element('He',1.0)
    helium.set_density('g/cm3',1.03*(10**-4))

    #stainless https://www.aesteiron.com/sa240-304l-stainless-steel-sheet-plate.html
    stainless = openmc.Material(name='stainless',temperature = operating_temp)
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
    boron = openmc.Material(name = 'boron',temperature = operating_temp)
    boron.add_element('B',4.0)
    boron.add_element('C',1.0)
    boron.set_density('g/cm3',2.52)

    #blanket
    blanket = openmc.Material(name = 'blanket',temperature = operating_temp)
    blanket.add_element('F',5.0)
    blanket.add_element('Li',1.0)
    blanket.add_element('Th',1.0)
    blanket.set_density('g/cm3',5.0)

    #shield
    shield = openmc.Material(name = 'iron',temperature = operating_temp)
    shield.add_element('Fe',1.0)
    shield.set_density('g/cm3',7.874)

    #filter
    filter = openmc.Material(name = 'air',temperature = operating_temp)
    filter.add_element('N',0.7803)
    filter.add_element('O',0.21)
    filter.add_element('Ar',0.93)
    filter.add_element('C',0.04*1./3)
    filter.add_element('O',0.04*2./3)
    filter.set_density('g/cm3',0.001225)


    mats = [salt,BeO,inconel,insulation,coolant,helium,stainless,boron]

    return mats
    # from ORNL-2264
