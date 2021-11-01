import matplotlib.pyplot as plt
import openmc
import numpy as np

###############################################################################
#rod worth simulation of ARE

#exports a .txt file with a k_eff at each position
###############################################################################

output_filename = 'k_effs.txt'

#equilibrium operating temperature in kelvin
operating_temp = 977.5944

def build_model(dagmc_file):
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
    coolant = openmc.Material(name='coolant')
    coolant.add_element('Na',1.0)
    coolant.set_density('g/cm3',0.78)

    #helium
    helium = openmc.Material(name='helium')
    helium.add_element('He',1.0)
    helium.set_density('g/cm3',1.03*(10**-4))

    #absorber
    boron = openmc.Material(name='boron')
    boron.add_element('B',4.0)
    boron.add_element('C',1.0)
    boron.set_density('g/cm3',2.52)

    #stainless
    stainless = openmc.Material(name='stainless')
    stainless.add_element('C',0.030,percent_type='wo')
    stainless.add_element('Mn',2.00,percent_type='wo')
    stainless.add_element('P',0.045,percent_type='wo')
    stainless.add_element('S',0.030,percent_type='wo')
    stainless.add_element('Si',0.75,percent_type='wo')
    stainless.add_element('Cr',18.00,percent_type='wo')
    stainless.add_element('Ni',8.0,percent_type='wo')
    stainless.add_element('N',0.1,percent_type='wo')
    stainless.set_density('g/cm3',8.5)

    mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron])
    mats.export_to_xml()

    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = 100
    settings.inactive = 10
    settings.particles = 10000
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(dagmc_file)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

shim_rod_positions = np.linspace(0,90,36)
h5m_filenames = ['h5m_files/rod_worth/ARE_pos_' + str(i)[0:2] + '.h5m' for i in shim_rod_positions]
k_effs_simulated = []

#writing to text file
k_file = open(output_filename, 'w+')

for filename in h5m_filenames:
    model = build_model(filename)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs_simulated.append(k_eff.nominal_value)
        k_file.write("%s\n" %k_eff.nominal_value)

k_file.close()

#plot from .txt file
k_file = open('k_effs_simulated.txt', 'r')
for k in k_file.readlines():
    k_effs_simulated.append(float(k))
k_file.close()
