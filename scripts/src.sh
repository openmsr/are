#!/bin/bash

set -ex

# remove remnants of other simulations
rm *.xml

python ./scripts/check_for_h5m.py
python ./scripts/ARE_criticality_approach.py
python ./scripts/ARE_criticality_approach_post.py
