#!/bin/bash

set -ex

# remove tallies xml so it doesn't interfere
rm -f tallies.xml

python ./scripts/check_for_h5m.py
python ./scripts/ARE_criticality_approach.py
python ./scripts/ARE_criticality_approach_post.py
