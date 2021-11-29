################################################################################
#openmc source install
################################################################################
#!/bin/bash
set -ex

#dagmc compile & install
./dagmc-install.sh
echo "Compiled & installed dagmc, proceeding..."

#nuclear_data_download
./nuclear_data-install.sh
echo "Downloaded & extracted nuclear data, proceeding..."

sudo yay -Syu --noconfirm --sudoloop python-lxml \
			             python-scipy \
			             python-pandas \
                                     python-h5py \
                                     python-matplotlib \
                                     python-uncertainties 

#source install
cd /opt
sudo git clone --recurse-submodules --single-branch --branch develop --depth 1 https://github.com/openmc-dev/openmc.git
cd openmc
sudo mkdir build
cd build
sudo cmake -Doptimize=on \
           -Ddagmc=ON \
           -DDAGMC_ROOT=$HOME/DAGMC \
           -DHDF5_PREFER_PARALLEL=off ..
sudo make install
cd /opt/openmc/
sudo python setup.py install
