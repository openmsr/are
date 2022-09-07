from materials import *
import openmc

def build_model(fuel_comp,h5m_filepath,nuclear_data=None):

    mats = openmc.Materials([fuel_comp,BeO,inconel,insulation,coolant,helium,stainless,boron])
    if nuclear_data:
        mats.cross_sections = nuclear_data
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

    dag_univ = openmc.DAGMCUniverse(h5m_filepath)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model
