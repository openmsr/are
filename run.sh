#!/bin/bash

set -ex

PS3='ARE simulations: '
options=("k eigenvalue" "geometry plot" "neutron flux" "photon flux"
         "criticality approach" "shim rod calibration" "all" "quit")
select opt in "${options[@]}"
do
    case $opt in
        "k eigenvalue")
            echo "running k eigenvalue simulation..." &&
            bash ./scripts/k.sh
            ;;
        "geometry plot")
            echo "plotting geometry..." &&
            bash ./scripts/gp.sh
            ;;
        "neutron flux")
            echo "generating neutron flux plot..." &&
            bash ./scripts/nf.sh
            ;;
        "photon flux")
            echo "generating photon flux plot..." &&
            bash ./scripts/pf.sh
            ;;
        "criticality approach")
            echo "criticality approach..." &&
            bash ./scripts/ca.sh
            ;;
        "shim rod calibration")
            echo "shim rod calibration..." &&
            bash ./scripts/src.sh
            ;;
        "all")
            echo "running all..." &&
            bash ./scripts/k.sh &&
            bash ./scripts/gp.sh &&
            bash ./scripts/nf.sh &&
            bash ./scripts/pf.sh &&
            bash ./scripts/ca.sh &&
            bash ./scripts/src.sh 
            ;;
        "quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
