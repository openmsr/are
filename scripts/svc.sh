#!/bin/bash

set -ex

if test -f "./h5m_files/ARE.h5m"; then
  python ./scripts/ARE_volume_calcs.py
else
  python ./step_to_hm5/step_to_hm5.py
  python ./scripts/ARE_volume_calcs.py
fi
