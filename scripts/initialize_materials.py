import sys
sys.path.append('/opt/openmc/')
import openmc


def create_materials(operating_temp):
    #ARE material definitions

    # halfnium concentration <50 ppm accoring to ORNL-4616, so 25 ppm assumed
    h = 0.0025

    #######################################################################
    #fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
    salt = openmc.Material(name='salt', temperature = operating_temp)
    salt.add_element('F',41.96,percent_type='wo')
    salt.add_element('Na',11.13,percent_type='wo')
    salt.add_element('Zr',34.52*(1.0-h),percent_type='wo')
    salt.add_element('Hf',34.52*(h),percent_type='wo')
    salt.add_nuclide('U235',11.57,percent_type='wo')
    salt.add_nuclide('U238',0.83,percent_type='wo')
    salt.set_density('g/cm3',3.3142201)

    #######################################################################
    #moderator blocks
    BeO = openmc.Material(name='BeO',temperature = operating_temp)

    # by ao, expressed in ppm
    BeO.add_element('Be',499792)
    BeO.add_element('O',499792)

    # impurities
    BeO.add_element('Si',330)
    BeO.add_element('Al',50)
    BeO.add_element('Pb',25)
    BeO.add_element('Ni',5)
    BeO.add_element('Mn',5)
    BeO.add_element('Co',1)

    # density with temperature and differential expansion adjustment
    lambda_BeO = 9.0e-6
    lambda_inconel = 14.4e-6
    temp_adj_BeO = 1/(1+lambda_BeO*operating_temp)
    diff_exp_adj = (1+lambda_BeO*operating_temp)/(1+lambda_inconel*operating_temp)
    BeO.set_density('g/cm3',2.75*temp_adj_BeO*diff_exp_adj)

    #######################################################################
    #inconel
    inconel = openmc.Material(name='inconel',temperature = operating_temp)

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
    inconel.add_element('N',0.0295,percent_type='wo')
    temp_adj_inconel = 1/(1+lambda_inconel*operating_temp)
    inconel.set_density('g/cm3',8.5*temp_adj_inconel)

    #insulation (diatomaceous earth)(ORNL1535 pg. 80)
    insulation = openmc.Material(name='insulation',temperature = operating_temp)
    insulation.add_element('Si',1)
    insulation.add_element('O',2)
    insulation.set_density('g/cm3',0.28832)

    #insulation.add_element('O',13)
    #insulation.add_element('Al',2)
    #insulation.add_element('Ca',1)
    #insulation.add_element('Fe',2)
    #insulation.add_element('K',2)
    #insulation.add_element('Na',2)
    #insulation.add_element('Ti',1)
    #insulation.set_density('g/cm3',2.24)

    #######################################################################
    #coolant
    coolant = openmc.Material(name='coolant',temperature = operating_temp)
    coolant.add_element('Na',1.0)
    coolant.set_density('g/cm3',0.78)

    #######################################################################
    #helium
    helium = openmc.Material(name='helium',temperature = operating_temp)
    helium.add_element('He',1.0)
    helium.set_density('g/cm3',1.03*(10**-4))

    #######################################################################
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
    stainless.set_density('g/cm3',8.5*temp_adj_inconel)

    #######################################################################
    #absorber
    lambda_boron = 4.6e-6
    temp_adj_boron = 1/(1+lambda_boron*operating_temp)
    boron = openmc.Material(name = 'boron',temperature = operating_temp)
    boron.add_element('B',4.0)
    boron.add_element('C',1.0)
    boron.set_density('g/cm3',2.52*temp_adj_boron)

    #######################################################################
    #blanket
    blanket = openmc.Material(name = 'blanket',temperature = operating_temp)
    blanket.add_element('F',5.0)
    blanket.add_element('Li',1.0)
    blanket.add_element('Th',1.0)
    blanket.set_density('g/cm3',5.0)

    #######################################################################
    #shield
    shield = openmc.Material(name = 'iron',temperature = operating_temp)
    shield.add_element('Fe',1.0)
    shield.set_density('g/cm3',7.874)

    mats = [salt,BeO,inconel,insulation,coolant,helium,stainless,boron]

    return mats
    # from ORNL-2264
