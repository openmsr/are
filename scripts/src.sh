#!/bin/bash

set -ex

# remove tallies xml so it doesn't interfere
rm -f tallies.xml

python ./scripts/check_for_h5m.py
python ./scripts/ARE_shim_rod_calibration.py
python ./scripts/ARE_shim_rod_calibration_post.py
