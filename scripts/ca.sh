#!/bin/bash

set -ex

# remove tallies xml so it doesn't interfere
rm -f tallies.xml

if test -f "./h5m_files/ARE_rods_35.h5m"; then
  python ./scripts/ARE_criticality_approach_2.py
  python ./scripts/ARE_criticality_approach_post.py
else
  python ./scripts/step_to_h5m_cubit.py /step_files/ARE_rods_35.step
  python ./scripts/ARE_criticality_approach_2.py
  python ./scripts/ARE_criticality_approach_post.py
fi
