#!/bin/bash

set -ex

if test -f "./h5m_files/ARE_gamma.h5m"; then
  python ./scripts/ARE_gamma_spectra.py
else
  python ./step_to_hm5/step_to_hm5_photon.py
  python ./scripts/ARE_gamma_spectra.py
fi
