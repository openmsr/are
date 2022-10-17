import sys
sys.path.append('/opt/openmc/')
import openmc


def make_fuel(na:float=0.0,
              zr:float=0.0,
              f:float=0.0,
              u235:float=0.0,
              u238:float=0.0,
              temp:float=0.0,
              density:float=0.0,
              enriched:float=0.0):

    """
    returns openmc material object representing fuel salt with
    the given weight percentages and uranium enrichment
    """

    #fuel salt NaF-ZrF4-UF4 0.5309-0.4073-0.0618 %mol
    salt = openmc.Material(name='salt', temperature = temp)
    salt.set_density('g/cm3',density)
    salt.add_element('Na',na,percent_type='wo')
    salt.add_element('Zr',zr,percent_type='wo')
    salt.add_element('F',f,percent_type='wo')
    salt.add_nuclide('U235',u235,percent_type='wo')
    salt.add_nuclide('U238',u238,percent_type='wo')

    return salt
