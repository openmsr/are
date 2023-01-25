#!/bin/bash

set -ex

bash ./scripts/k.sh 
bash ./scripts/gp.sh
bash ./scripts/nf.sh
bash ./scripts/pf.sh
bash ./scripts/ca.sh
bash ./scripts/src.sh
