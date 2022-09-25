#!/bin/bash

set -ex

python ./scripts/check_for_h5m.py
python ./scripts/ARE_criticality_approach.py
python ./scripts/ARE_criticality_approach_post.py
