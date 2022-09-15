from initialize_materials import create_materials
import openmc

def build_model(h5m_filepath,fuel=None,nuclear_data=None,operating_temp=977.59):

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
    settings.batches = 100
    settings.inactive = 10
    settings.particles = 10000
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model
