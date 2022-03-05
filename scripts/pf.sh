#!/bin/bash

set -ex

if test -f "./h5m_files/ARE.h5m"; then
  python ./scripts/ARE_photon_flux.py
else
  python ./step_to_hm5/step_to_hm5.py
  python ./scripts/ARE_photon_flux.py
