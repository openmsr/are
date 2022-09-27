#!/bin/bash

set -ex

# remove remnants of other simulations
rm *.xml

if test -f "./h5m_files/ARE_rods_35.h5m"; then
  python ./scripts/ARE_photon_flux.py
else
  python ./scripts/step_to_h5m.py ./step_files/ARE_rods_35.step
  python ./scripts/ARE_photon_flux.py
fi
