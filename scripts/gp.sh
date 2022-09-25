#!/bin/bash

set -ex

if test -f "./h5m_files/ARE_rods_35.h5m"; then
  python ./scripts/ARE_geometry_plot.py
else
  python ./scripts/step_to_h5m.py ./step_files/ARE_rods_35.step
  python ./scripts/ARE_geometry_plot.py
fi
