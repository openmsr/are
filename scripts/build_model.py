from initialize_materials import create_materials
import openmc

def build_model(h5m_filepath,fuel=None,nuclear_data=None,operating_temp=977.59,batches=100,inactive=10,particles=10000):

    mats = create_materials(operating_temp)
    if fuel:
        mats = [m for m in mats if m.name != 'salt']
        mats.append(fuel)
    mats_openmc = openmc.Materials(mats)
    if nuclear_data:
        mats_openmc.cross_sections = nuclear_data

    mats_openmc.export_to_xml()
    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = batches
    settings.inactive = inactive
    settings.particles = particles
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

def build_fuel_model(h5m_filepath,T_f=977.59,fuel=None,nuclear_data=None,operating_temp=977.59,batches=100,inactive=10,particles=10000):

    mats = create_materials(operating_temp,fuel_temp = T_f)
    if fuel:
        mats = [m for m in mats if m.name != 'salt']
        mats.append(fuel)
    mats_openmc = openmc.Materials(mats)
    if nuclear_data:
        mats_openmc.cross_sections = nuclear_data

    mats_openmc.export_to_xml()
    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = batches
    settings.inactive = inactive
    settings.particles = particles
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    # settings.verbosity = 10
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

def build_coolant_model(h5m_filepath,coolant_temp=977.59,fuel=None,nuclear_data=None,operating_temp=977.59,batches=100,inactive=10,particles=10000):

    mats = create_materials(operating_temp,c_temp = coolant_temp)
    if fuel:
        mats = [m for m in mats if m.name != 'salt']
        mats.append(fuel)
    mats_openmc = openmc.Materials(mats)
    if nuclear_data:
        mats_openmc.cross_sections = nuclear_data

    mats_openmc.export_to_xml()
    settings = openmc.Settings()
    # settings.temperature = {'method':'interpolation'}
    settings.temperature = {'method':'multipole'}
    settings.batches = batches
    settings.inactive = inactive
    settings.particles = particles
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    # settings.verbosity = 10
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

def build_moderator_model(h5m_filepath,mod_temp=977.59,fuel=None,nuclear_data=None,operating_temp=977.59,batches=100,inactive=10,particles=10000):

    mats = create_materials(operating_temp,Tm=mod_temp)
    if fuel:
        mats = [m for m in mats if m.name != 'salt']
        mats.append(fuel)
    mats_openmc = openmc.Materials(mats)
    if nuclear_data:
        mats_openmc.cross_sections = nuclear_data

    mats_openmc.export_to_xml()
    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = batches
    settings.inactive = inactive
    settings.particles = particles
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    # settings.verbosity = 10
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model