import os
from build_model import build_model
import openmc
from fuel_salts import salt_8A,salt_9B,salt_10C,salt_11C,salt_12B
from initialize_materials import create_materials

# Import h5m files
core_h5m = './h5m_files/ARE_pos_0..h5m'
cr_h5m = './h5m_files/single_control_rod.h5m'
#reg_h5m = './h5m_files/regulating_rod.h5m'
salts = [salt_8A,salt_9B,salt_10C,salt_11C,salt_12B]
positions = [20,25,30,35]

operating_temp = 977

# store set of k_effs for each fuel concentration
k_effs = []

output_filename = "src_k.txt"

# calibration was run against 14 different fuel concentrations
# loop through each fuel concentrations
# loop through each position
for s in salts:
    k_pos = []
    for p in positions:

        # Create DAGMC universes out of h5m files
        core = openmc.DAGMCUniverse(filename=core_h5m, auto_geom_ids=True, universe_id=1)
        cr = openmc.DAGMCUniverse(filename=cr_h5m, auto_geom_ids=True, universe_id=2)
        #reg = openmc.DAGMCUniverse(filename=reg_h5m, auto_geom_ids=True, universe_id=3)

        # Create regions
        core_region = core.bounding_region()
        cr1_region = cr.bounding_region(boundary_type='transmission', starting_id=20000)

        # Extend control rod region, to include upwards translations
        cr1_region = cr1_region | cr1_region.translate([0,0,100])

        # Create control rod region 2 and 3 as translated region of control rod 1
        cr2_region = cr1_region.translate([2.54*i for i in [6.495,-11.25,0]])
        cr3_region = cr1_region.translate([2.54*i for i in [-6.495,-11.25,0]])
        #reg_region = cr1_region.translate([2.54*i for i in [0,-7.5,0]])

        # Create openmc Cells 
        core_cell = openmc.Cell(region=~(cr1_region | cr2_region | cr3_region) & core_region , fill=core)
        cr1_cell = openmc.Cell(name='CR1', region=cr1_region, fill=cr)
        cr2_cell = openmc.Cell(name='CR2', region=cr2_region, fill=cr)
        cr3_cell = openmc.Cell(name='CR3', region=cr3_region, fill=cr)
        #reg_cell = openmc.Cell(name='REG', region=reg_region, fill=reg)
            
        #translate control rods at top position (fully withdrawn)
        inch_to_cm = 2.54
        setattr(cr1_cell, 'translation', [0, 0, p*inch_to_cm])
        setattr(cr2_cell, 'translation', [0, 0, p*inch_to_cm])
        setattr(cr3_cell, 'translation', [0, 0, p*inch_to_cm])
        #setattr(reg_cell, 'translation', [0, 0, p*inch_to_cm])

        # Create openmc Geometry object
        geometry = openmc.Geometry([core_cell,cr1_cell,cr2_cell,cr3_cell])

        mats = create_materials(operating_temp)
        mats = [m for m in mats if m.name != 'salt']
        mats.append(s)
        mats_openmc = openmc.Materials(mats)

        mats_openmc.export_to_xml()
        geometry.export_to_xml()

        settings = openmc.Settings()
        settings.temperature = {'method':'interpolation'}
        settings.batches = 120
        settings.inactive = 20
        settings.particles = 10000
        settings.export_to_xml()
        source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
        settings.source = openmc.Source(space=source_area)
        settings.export_to_xml()

        model = openmc.model.Model(geometry,mats,settings)
        sp_filepath = model.run(output = True)

        with openmc.StatePoint(sp_filepath) as sp:
            k_eff = sp.k_combined
            k_pos.append(k_eff.nominal_value)
    k_effs.append(k_pos)

results = open(output_filename,'w+')
for l in k_effs:
    for i in l:
        results.write(f"{i} ")
    results.write("\n")
results.close()
















