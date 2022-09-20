#!/bin/bash

set -ex

if test -f "./h5m_files/ARE_rods_35.h5m"; then
  python ./scripts/ARE_criticality_approach.py
  python ./scripts/ARE_criticality_approach_post.py
else
  python ./scripts/step_to_h5m_cubit.py
  python ./scripts/ARE_criticality_approach.py
  python ./scripts/ARE_criticality_approach_post.py
fi