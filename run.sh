#!/bin/bash

#!/bin/bash

PS3='ARE simulations: '
options=("k eigenvalue" "geometry plot" "neutron flux" "photon flux"
          "gamma spectra" "rod worth" "stochastic volume calculations" "quit")
select opt in "${options[@]}"
do
    case $opt in
        "k eigenvalue")
            echo "running k eigenvalue simulation..."
            if test -f "./h5m_files/ARE.h5m"; then
              python ./scripts/ARE.py
            else
              python ./step_to_hm5/step_to_hm5.py
              python ./scripts/ARE.py
            ;;
        "geometry plot")
            echo "plotting geometry..."
            if test -f "./h5m_files/ARE.h5m"; then
              python ./scripts/ARE_geometry_plot.py
            else
              python ./step_to_hm5/step_to_hm5.py
              python ./scripts/ARE_geometry_plot.py
            ;;
        "neutron flux")
            echo "generating neutron flux plot..."
            if test -f "./h5m_files/ARE.h5m"; then
              python ./scripts/ARE_neutron_flux.py
            else
              python ./step_to_hm5/step_to_hm5.py
              python ./scripts/ARE_neutron_flux.py
            ;;
        "photon flux")
            echo "generating photon flux plot..."
            if test -f "./h5m_files/ARE.h5m"; then
              python ./scripts/ARE_photon_flux.py
            else
              python ./step_to_hm5/step_to_hm5.py
              python ./scripts/ARE_photon_flux.py
            ;;
        "gamma spectra")
            echo "generating gamma spectra..."
            if test -f "./h5m_files/ARE_gamma.h5m"; then
              python ./scripts/ARE_gamma_spectra.py
            else
              python ./step_to_hm5/step_to_hm5_photon.py
              python ./scripts/ARE_gamma_spectra.py
            ;;
        "rod worth")
            echo "generating rod worth plot..."
            count=$(ls -1q h5m_files/rod_worth* | wc -l)
            if [$count=36]; then
              python ./scripts/ARE_rod_worth.py
              python ./scripts/ARE_rod_worth_post.py
            elif [$count=0]; then
              python ./step_to_hm5/step_to_hm5_rod_worth.py
              python ./scripts/ARE_rod_worth.py
              python ./scripts/ARE_rod_worth_post.py
            else
              echo "rod worth directory incomplete"
              break
            ;;
        "stochastic volume calculations")
            echo "stochastic volume calculations..."
            if test -f "./h5m_files/ARE.h5m"; then
              python ./scripts/ARE_volume_calcs.py
            else
              python ./step_to_hm5/step_to_hm5.py
              python ./scripts/ARE_volume_calcs.py
            ;;
        "quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
