#!/bin/bash

set -ex

# remove tallies xml so it doesn't interfere
rm -f tallies.xml

if test -f "./h5m_files/ARE_gamma.h5m"; then
  python ./scripts/ARE_gamma_spectra.py
else
  python ./step_to_h5m/step_to_h5m_photon.py
  python ./scripts/ARE_gamma_spectra.py
  python ./scripts/ARE_gamma_spectra_plotter.py
fi
