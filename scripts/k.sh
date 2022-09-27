#!/bin/bash

set -ex

if test -f "./h5m_files/ARE_rods_35.h5m"
then
  python ./scripts/ARE.py
else
  python ./scripts/step_to_h5m_cubit.py /step_files/ARE_rods_35.step
  python ./scripts/ARE.py
fi
