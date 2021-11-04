import matplotlib.pyplot as plt
import openmc
from collections import namedtuple
import spectrum_plotter

#simulation results
statepoint_filename = 'statepoint.100.h5'

#filename for spectrum plot
plot_filename = 'spectra/spectra_overlay_opp_6.png'

#energy groups
energy_bins = openmc.mgxs.GROUP_STRUCTURES['VITAMIN-J-175']

#using namedtuple structure to store spectrum data and corresponding volume
Spectrum = namedtuple('Spectrum',['name','volume','tally'])

from plotting_utils import create_plotly_figure, add_trace_to_figure

# open the results file
results = openmc.StatePoint(statepoint_filename)

spectra_list = []

#fuel salt
cell_tally_1 =  results.get_tally(name='salt_spectrum')
salt_spectrum = Spectrum(name = 'salt_spectrum',volume = 67396.413, tally = cell_tally_1)
spectra_list.append(salt_spectrum)

#moderator
cell_tally_2 = results.get_tally(name='moderator_spectrum')
moderator_spectrum = Spectrum(name = 'moderator_spectrum',volume = 95703.739, tally = cell_tally_2)
spectra_list.append(moderator_spectrum)

#inconel assembly
cell_tally_3 = results.get_tally(name='inconel_spectrum')
inconel_spectrum = Spectrum(name = 'inconel_spectrum',volume = 3093469.87198, tally = cell_tally_3)
spectra_list.append(inconel_spectrum)

#insulation in sleeves
#cell_tally_4 = results.get_tally(name='cell_spectra_tally_4')

#coolant
cell_tally_5 = results.get_tally(name='coolant_spectrum')
coolant_spectrum = Spectrum(name = 'coolant_spectrum',volume = 272469.76749999996, tally = cell_tally_5)
spectra_list.append(coolant_spectrum)

#helium
cell_tally_6 = results.get_tally(name='helium_spectrum')
helium_spectrum = Spectrum(name = 'helium_spectrum',volume = 38441176.6459, tally = cell_tally_6)
spectra_list.append(helium_spectrum)

#stainless (regulating rod slugs and casing)
cell_tally_7 = results.get_tally(name='stainless_spectrum')
stainless_spectrum = Spectrum(name = 'stainless_spectrum',volume = 4633.3469000000005, tally = cell_tally_7)
spectra_list.append(stainless_spectrum)

#boron
cell_tally_8 = results.get_tally(name='boron_spectrum')
boron_spectrum = Spectrum(name = 'boron_spectrum',volume = 2549.6562, tally = cell_tally_8)
spectra_list.append(boron_spectrum)

#blanket
cell_tally_9 = results.get_tally(name='blanket_spectrum')
blanket_spectrum = Spectrum(name = 'blanket_spectrum',volume = 2397475.018, tally = cell_tally_9)
spectra_list.append(blanket_spectrum)

#shield
cell_tally_10 = results.get_tally(name='shield_spectrum')
shield_spectrum = Spectrum(name = 'shield_spectrum',volume = 2947253.732, tally = cell_tally_10)
spectra_list.append(shield_spectrum)

#air (outer filter)
cell_tally_11 = results.get_tally(name='filter_spectrum')
filter_spectrum = Spectrum(name = 'filter_spectrum',volume = 6445.385736, tally = cell_tally_11)
spectra_list.append(filter_spectrum)



test_plot = spectrum_plotter.plot_spectrum_from_tally(
    spectrum = results.tallies,
    required_units="1 / centimeter ** 2",
    x_label="Energy [MeV]",
    y_label="Flux [n/cm^2s]",
    x_scale="linear",
    y_scale="linear",
    title="ARE_spectra",
    filename=plot_filename,
    volume = 10
)
